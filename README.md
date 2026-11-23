# AQA Portfolio

![Python](https://img.shields.io/badge/python-3.12-blue)

Python-based test automation engineering portfolio, built on 8 years of
Manual QA experience in outsourced IT (mobile and web applications).

## About

This repository documents the technical automation layer I'm building on
top of an established QA background — Python fundamentals, pytest,
Playwright, and API testing, applied through realistic, self-designed
test scenarios rather than generic tutorials. Later phases add CI/CD and
a security-testing specialization, developed toward future work in
systems and defense-adjacent QA roles.

## Tech Stack

- Python 3.12
- uv (dependency management)
- pytest, Playwright (upcoming)
- Ruff (linting/formatting)
- pymavlink (hardware-sim testing against ArduPilot SITL)

## Setup

\`\`\`bash
git clone git@github.com:Marildi/aqa-portfolio.git
cd aqa-portfolio
uv sync
\`\`\`

## Project Structure

\`\`\`
aqa-portfolio/
├── tests/                 # pytest suites: UI (Playwright), API, DB, security
│   ├── conftest.py        # shared fixtures
│   ├── test_bola.py       # security: BOLA access control
│   ├── test_auth_patterns.py   # API key + JWT
│   ├── test_database.py   # SQL + injection checks
│   ├── test_sitl_telemetry.py  # ArduPilot SITL: telemetry + failsafe fault-injection
│   └── test_*_flows.py    # Playwright UI flows (page objects)
├── pages/                 # Page Object Model classes
├── utils/                 # helpers, incl. orders_api.py (BOLA demo)
├── sql/                   # SQL exercises and schema
├── docs/                  # security_test_report.md and notes
├── locustfile.py          # load testing
├── Dockerfile
└── .github/workflows/     # CI: tests (matrix), ZAP scan, notifications
\`\`\`

## Security + Functional Testing

Functional tests check the app works for the people it's meant for; security tests check it doesn't work for anyone else. I test both on the same features:

| Feature | Functional test (works for the right user) | Security test (blocks the wrong one) |
|---|---|---|
| Orders API | `test_order_access[owner_bob]`: owner sees own order | `test_order_access[stranger_blocked]`: stranger gets 404 (BOLA) |
| Database | `test_insert_new_pilot_persists`: valid insert is saved | `test_hostile_name_is_stored_as_plain_text`: SQL injection payload is stored as text, not executed |
| JWT auth | `test_valid_token_decodes_successfully` | `test_expired_token_raises_error`, `test_tampered_token_raises_error` |
| Login (UI) | `test_login_success` | `test_login_failures`: identical error for wrong password and unknown user (no user enumeration) |

Security tests are tagged `@pytest.mark.security` (`uv run pytest -m security`). Findings are in [docs/security_test_report.md](docs/security_test_report.md); CI also runs a ZAP baseline scan against Juice Shop.

## Hardware-in-the-Loop Testing

Beyond software-only testing: automated pytest tests against a real ArduPilot flight-controller build, running in a container ([setup](docs/sitl_setup.md)), talking MAVLink. Fault-injection tests (GPS loss, battery-critical) verify ArduPilot's actual safety response, not just telemetry values — see [docs/mavlink_notes.md](docs/mavlink_notes.md) for details and one non-obvious finding from debugging it.

## Progress

- [x] Phase 0 — Environment & Python Fundamentals
- [x] Phase 1 — Intermediate Python
- [x] Phase 2 — Git, Command Line & Dev Practices (in progress)
- [x] Phase 3 — Pytest and Testing Fundamentals
- [x] Phase 4 — Playwright (Python)
- [x] Phase 5 — API Testing
- [x] Phase 6 — CI/CD, Docker & Cloud
- [x] Phase 7 — SQL, Performance & Security Testing
- [ ] Phase 8 — Systems Engineering & Aerospace/Defense Layer
- [ ] Phase 9 — Portfolio, Positioning & Contract-Readiness
