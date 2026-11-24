FROM ardupilot:latest

USER root
WORKDIR /ardupilot

RUN rm -rf /ardupilot/* /ardupilot/.[!.]* 2>/dev/null; \
    git clone --recurse-submodules https://github.com/ArduPilot/ardupilot .

RUN git config --global --add safe.directory '*' \
    && apt-get update \
    && apt-get install -y --no-install-recommends python3-pip \
    && python3 -m pip install --break-system-packages empy==3.3.4 \
    && ./waf configure --board sitl \
    && ./waf copter

EXPOSE 5760

CMD ["Tools/autotest/sim_vehicle.py", "-v", "ArduCopter", "--no-mavproxy", "--no-rebuild", "-j4"]
