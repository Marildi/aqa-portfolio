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
