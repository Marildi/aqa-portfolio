# Security Test Report

Scope: manual and automated checks of BOLA, SQL injection, JWT key strength and a ZAP baseline scan. All targets are practice or simulated systems (a local in-memory orders API, an in-memory SQLite DB, OWASP Juice Shop in Docker), not production.

| ID | Finding | Severity | Evidence | Remediation | Status |
|----|---------|----------|----------|-------------|--------|
| SEC-01 | BOLA: `get_order_vulnerable` returns any user's order if the ID is known (bob reads alice's order `001`) | High | `get_order_vulnerable("bob","001")` → `{'status_code': 200, 'body': {'owner': 'alice', ...}}`; test: `test_vulnerable_version_leaks_other_users_order` (strict xfail)| `get_order_secure` checks `order["owner"] == current_user` and returns 404 for others (no existence leak). Covered by `test_order_access[stranger_blocked]` | Fixed in secure version; vulnerable version kept as a demo |
| SEC-02 | JWT signing key too short: 15 bytes, below the 32 recommended for HS256 | Low (test key) / High if in production | PyJWT key-length warning on `tests/test_auth_patterns.py`; key lengthened to 32+ bytes | Use a key of 32+ random bytes; load it from env/secrets, never hardcode | Fixed |
| SEC-03 | ZAP baseline on Juice Shop: Content-Security-Policy header not set | Medium (ZAP rating) | `WARN-NEW: Content Security Policy (CSP) Header Not Set [10038] x 5` (CWE-693); report in CI artifact `zap-report` | Send a `Content-Security-Policy` header from the server | Open (practice target, not ours to fix) |

**Checks that passed:** SQL injection payloads (`'; DROP TABLE ...`, `' OR '1'='1`) were stored or matched as plain text because queries use `?` parameters (`tests/test_database.py`).
