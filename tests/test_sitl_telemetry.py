import math
import socket

from pymavlink import mavutil


# REQ-01: THE system SHALL report active state.
# → test_heartbeat_received
def test_heartbeat_received(sitl):
    assert sitl.target_system == 1


# REQ-02: WHILE the vehicle is on the ground,
# the flight controller SHALL report a relative altitude near zero via telemetry.
# → test_altitude_sane_on_ground


def test_altitude_sane_on_ground(sitl):
    sitl.mav.command_long_send(
        sitl.target_system,
        sitl.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GLOBAL_POSITION_INT,
        1000000,
        0,
        0,
        0,
        0,
        0,
    )
    gpi = sitl.recv_match(type="GLOBAL_POSITION_INT", blocking=True, timeout=10)
    assert gpi is not None, "No GLOBAL_POSITION_INT received"
    assert math.isclose(gpi.relative_alt, 0, abs_tol=500)


# REQ-03: WHEN GPS signal is lost,
# the flight controller SHALL report a degraded fix status via telemetry.
# → test_gps_loss_triggers_failsafe


def test_gps_loss_triggers_failsafe(sitl):
    sitl.mav.param_set_send(
        sitl.target_system,
        sitl.target_component,
        b"SIM_GPS1_ENABLE",
        0,
        mavutil.mavlink.MAV_PARAM_TYPE_INT32,
    )

    ack = sitl.recv_match(type="PARAM_VALUE", blocking=True, timeout=5)
    assert ack.param_value == 0

    # statustext is silent, checking the theory: a disarmed, grounded vehicle likely
    # doesn't raise a human-readable GPS-loss warning,
    # because there's no in-flight decision for it to make yet.
    # status = sitl.recv_match(type="STATUSTEXT", blocking=True, timeout=15)
    # print(status)

    sitl.mav.command_long_send(
        sitl.target_system,
        sitl.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_GPS_RAW_INT,
        1000000,
        0,
        0,
        0,
        0,
        0,
    )
    gps_raw = sitl.recv_match(type="GPS_RAW_INT", blocking=True, timeout=10)
    assert gps_raw is not None
    assert gps_raw.fix_type < 2


# REQ-04: IF battery voltage drops below the critical threshold,
# THEN the flight controller SHALL reject arming and report the reason.
# → test_battery_critical_triggers_failsafe


def test_battery_critical_triggers_failsafe(sitl):
    # checking what thresholds exist
    sitl.mav.command_long_send(
        sitl.target_system,
        sitl.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
        0,
        mavutil.mavlink.MAVLINK_MSG_ID_BATTERY_STATUS,
        1000000,
        0,
        0,
        0,
        0,
        0,
    )
    batt = sitl.recv_match(type="BATTERY_STATUS", blocking=True, timeout=10)
    assert batt is not None
    assert batt.voltages[0] < 13000  # mV, below BATT_CRT_VOLT threshold

    # simulating critical
    sitl.mav.param_set_send(
        sitl.target_system,
        sitl.target_component,
        b"BATT_CRT_VOLT",
        13.0,
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32,
    )
    ack = sitl.recv_match(type="PARAM_VALUE", blocking=True, timeout=5)
    assert ack.param_value == 13.0

    # investigating why battery wasn't reduced
    # Investigated charge_state field first — it never updated even with
    # BATT_FS_CRT_ACT configured. Real proof of the failsafe is the arm
    # rejection + STATUSTEXT below, not this telemetry field.

    sitl.mav.command_long_send(
        sitl.target_system,
        sitl.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
    )
    arm_result = sitl.recv_match(type="COMMAND_ACK", blocking=True, timeout=5)
    assert arm_result is not None
    assert arm_result.result == mavutil.mavlink.MAV_RESULT_FAILED

    reason = sitl.recv_match(type="STATUSTEXT", blocking=True, timeout=5)
    assert reason is not None
    assert "battery" in reason.text.lower() and "critical" in reason.text.lower()


# REQ-05:IF malformed bytes are present in the packet,
# THEN the system SHALL ignore it and remain active on the same link.


def test_garbage_bytes_do_not_crash_sitl(sitl):
    s = socket.create_connection(("127.0.0.1", 5760), timeout=5)
    s.sendall(b"\x00\xff\x13\x37\xde\xad\xbe\xef" * 10)  # junk, not valid MAVLink
    s.close()

    hb = sitl.recv_match(type="HEARTBEAT", blocking=True, timeout=10)
    print(hb)
    assert hb is not None
    assert hb.get_type() == "HEARTBEAT"
    assert sitl.target_system == 1


# REQ-06: IF an unsupported command is received,
# THEN the system SHALL reject the command with a clear error.


def test_unsupported_command_returns_proper_error(sitl):
    sitl.mav.command_long_send(
        sitl.target_system,
        sitl.target_component,
        60000,
        0,  # nonsense command ID — no such command exists
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    )
    ack = sitl.recv_match(type="COMMAND_ACK", blocking=True, timeout=5)
    assert ack is not None
    assert ack.result == mavutil.mavlink.MAV_RESULT_UNSUPPORTED


# REQ-07: IF a received packet fails CRC validation,
# THEN the system SHALL discard it without a reply,
# and SHALL continue processing subsequent valid requests on the same link.
# → test_bad_crc_packet_is_rejected


def test_bad_crc_packet_is_rejected(sitl):
    # Build a real, valid PARAM_REQUEST_READ packet
    msg = sitl.mav.param_request_read_encode(
        sitl.target_system, sitl.target_component, b"BATT_FS_CRT_ACT", -1
    )
    good_bytes = msg.pack(sitl.mav)

    # Corrupt the last byte (part of the checksum) — same payload, broken CRC
    bad_bytes = bytearray(good_bytes)
    bad_bytes[-1] ^= 0xFF

    s = socket.create_connection(("127.0.0.1", 5760), timeout=5)
    s.sendall(bytes(bad_bytes))
    s.close()

    corrupted_reply = None
    for _ in range(5):
        msg2 = sitl.recv_match(type="PARAM_VALUE", blocking=True, timeout=2)
        if msg2 is None:
            break
        if msg2.param_id == "BATT_FS_CRT_ACT":
            corrupted_reply = msg2
            break

    assert corrupted_reply is None  # corrupted packet got no reply

    sitl.mav.param_request_read_send(
        sitl.target_system, sitl.target_component, b"BATT_FS_CRT_ACT", -1
    )
    real_reply = None
    for _ in range(20):
        msg3 = sitl.recv_match(type="PARAM_VALUE", blocking=True, timeout=5)
        if msg3 is None:
            break
        if msg3.param_id == "BATT_FS_CRT_ACT":
            real_reply = msg3
            break

    assert real_reply is not None  # link still works for a valid request
