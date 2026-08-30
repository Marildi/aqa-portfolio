# Step 69: API test suite against the OpenSky Network API

import requests

BASE_URL = "https://opensky-network.org/api"


def test_get_all_states_anonymous():
    response = requests.get(f"{BASE_URL}/states/all")
    assert response.status_code == 200
    data = response.json()
    assert "states" in data
    assert "time" in data


def test_state_vector_structure():
    response = requests.get(f"{BASE_URL}/states/all")
    data = response.json()
    states = data["states"]
    assert len(states) > 0

    first_aircraft = states[0]
    icao24 = first_aircraft[0]  # transponder address
    callsign = first_aircraft[1]  # flight callsign
    origin_country = first_aircraft[2]
    longitude = first_aircraft[5]
    latitude = first_aircraft[6]
    altitude = first_aircraft[7]

    assert isinstance(icao24, str)
    assert isinstance(callsign, str) or callsign is None
    assert isinstance(origin_country, str)
    assert isinstance(longitude, (int, float)) or longitude is None
    assert isinstance(latitude, (int, float)) or latitude is None
    assert isinstance(altitude, (int, float)) or altitude is None


def test_states_within_bounding_box():
    params = {
        "lamin": 36.8,
        "lamax": 42.2,
        "lomin": -9.6,
        "lomax": -6.1,
    }
    response = requests.get(f"{BASE_URL}/states/all", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["states"] is not None or data["states"] == []


def test_rate_limit_headers_present():
    response = requests.get(f"{BASE_URL}/states/all")
    assert "X-Rate-Limit-Remaining" in response.headers
    remaining = int(response.headers["X-Rate-Limit-Remaining"])
    assert remaining >= 0
    print(f"Rate limit remaining: {remaining}")
