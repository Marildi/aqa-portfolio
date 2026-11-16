# ArduPilot SITL setup (Docker)

Simulated ArduCopter running in a container, built from the official ArduPilot source (commit `a995235cda`), checked via MAVLink heartbeat.

## Commands

```bash
# 1. Clone official source (outside this repo)
git clone --recurse-submodules https://github.com/ArduPilot/ardupilot
cd ardupilot

# 2. Build the official Dockerfile (~15 min)
docker build . -t ardupilot --build-arg USER_UID=$(id -u) --build-arg USER_GID=$(id -g)

# 3. Start container, MAVLink port on localhost only
docker run --rm -it -v "$(pwd)":/ardupilot -p 127.0.0.1:5760:5760 ardupilot:latest bash

# 4. Inside the container: build and start SITL
Tools/autotest/sim_vehicle.py -v ArduCopter --no-mavproxy -j4

# 5. On the host (second terminal): connect with pymavlink
uv run --with pymavlink python
```

```python
from pymavlink import mavutil
m = mavutil.mavlink_connection("tcp:127.0.0.1:5760")
m.wait_heartbeat()                                  # drone is alive
hb = m.recv_match(type="HEARTBEAT", blocking=True)  # read the message
```

Result: heartbeat received, system ID 1.

## Security notes

- Official ArduPilot source and Dockerfile instead of an unverified community image (single-maintainer account, no verified-publisher badge, old default ArduPilot version).
- Container runs as a non-root user.
- MAVLink port bound to `127.0.0.1` only, since the endpoint has no authentication.
- Accepted risk: the official Dockerfile grants passwordless sudo inside the container. Acceptable for a throwaway local simulator; not for production images.
