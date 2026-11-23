
**Requirements traceability matrix (RTM)**

| Req ID | Requirement | Test | Result |
|--------|-------------|------|--------|
| REQ-01 | THE system SHALL report active state. | test_heartbeat_received | PASS |
| REQ-02 | WHILE the vehicle is on the ground, the flight controller SHALL report a relative altitude near zero via telemetry. | test_altitude_sane_on_ground | PASS |
| REQ-03 | WHEN GPS signal is lost, the flight controller SHALL report a degraded fix status via telemetry. | test_gps_loss_triggers_failsafe | PASS |
| REQ-04 | IF battery voltage drops below the critical threshold, THEN the flight controller SHALL reject arming and report the reason. | test_battery_critical_triggers_failsafe | PASS |
| REQ-05 | IF malformed bytes are present in the packet, THEN the system SHALL ignore it and remain active on the same link. | test_garbage_bytes_do_not_crash_sitl | PASS |
| REQ-06 | IF an unsupported command is received, THEN the system SHALL reject the command with a clear error. | test_unsupported_command_returns_proper_error | PASS |
| REQ-07 | IF a received packet fails CRC validation, THEN the system SHALL discard it without a reply, and SHALL continue processing subsequent valid requests on the same link. | test_bad_crc_packet_is_rejected | PASS |

**Note:** RTM created in non-standard way test → inferred requirement. That is intentional as a part of learning process. Usual approach is requirement → derived test.
