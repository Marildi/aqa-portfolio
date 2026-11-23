# MAVLink Basics — Notes

## Message structure
MAVLink 2 packet: start byte → payload length → flags → sequence → system ID / component ID (sender's address) → message ID (which type) → payload (the fields) → checksum → optional signature.

## Message types explored
| Message | Purpose |
|---|---|
| `HEARTBEAT` | Liveness, vehicle type, mode, armed state |
| `COMMAND_LONG` / `COMMAND_ACK` | Request a specific action / vehicle's response |
| `GLOBAL_POSITION_INT` | Lat/lon (×1e7), altitude (mm), velocity, heading |
| `TIMESYNC` | Clock sync between GCS and vehicle |

## Lesson learned
Telemetry isn't pushed automatically. A ground station must explicitly request each message type and rate via `MAV_CMD_SET_MESSAGE_INTERVAL` — sending a heartbeat alone wasn't enough on this ArduPilot build. Confirmed in a local SITL session (ArduCopter, official ArduPilot source, container-isolated, `127.0.0.1`-only).

## Security note
Explored MAVLink's trust model while validating telemetry handling: message authentication is not on by default, and signing (MAVLink 2) is opt-in. Threat-model notes available on request.

## Automated tests against SITL (pymavlink)

Three pytest tests in `tests/test_sitl_telemetry.py`, against a locally running SITL instance (see `sitl_setup.md`):

| Test | Verifies |
|---|---|
| `test_heartbeat_received` | Connection to the vehicle is live |
| `test_altitude_sane_on_ground` | `GLOBAL_POSITION_INT.relative_alt` is near 0 while grounded |
| `test_gps_loss_triggers_failsafe` | Setting `SIM_GPS1_ENABLE=0` actually degrades `GPS_RAW_INT.fix_type` |
| `test_battery_critical_triggers_failsafe` | Setting `BATT_CRT_VOLT` above the real voltage blocks arming, with the correct reason in `STATUSTEXT` |

**Non-obvious finding:** for the battery case, ArduPilot's `BATTERY_STATUS.charge_state` field never updated, even with a failsafe action (`BATT_FS_CRT_ACT`) configured. The fault *was* detected — the proof was the vehicle refusing to arm and `STATUSTEXT` naming "Battery 1 critical voltage failsafe," not the telemetry field I expected to show it. Lesson: don't assume the obvious status field reflects internal state — verify against the system's actual behavior.
