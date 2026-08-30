# Step 70: Combining UI + API Tests in One Framework
# The pattern

# Setting up test preconditions purely through the UI is slow and brittle — every login, click, and page load adds time and a new chance for a flaky failure, even when that setup isn't actually what the test is trying to verify. The practical fix: use fast, direct API calls (or other backend shortcuts) to get the application into the state you need, and reserve actual browser interaction for the specific behavior under test.

# Example shape, in a real application with a backend API:

# def test_checkout_flow_with_api_setup(authenticated_page, api_session):
#     # FAST setup via API - not what we're testing, just getting to the starting point
#     api_session.post(f"{BASE_URL}/cart/items", json={"product_id": "abc", "qty": 1})

#     # SLOW, but this IS what we're testing
#     authenticated_page.goto("https://example.com/cart")
#     ...

# Why this matters
# Cuts test runtime significantly across a large suite
# Reduces flakiness, since fewer UI steps means fewer places for auto-waiting/timing issues to creep in (see step 43, step 48)
# Keeps each test focused on the one thing it's actually verifying, rather than re-proving unrelated setup steps work every single time
# Why this wasn't demonstrated directly against SauceDemo

# SauceDemo has no public API tied to its UI state (no way to seed the cart or session via a backend call) - it's a static demo app, not a real product. Forcing this pattern onto it would mean faking a nonexistent API, which wouldn't actually prove anything real.

# The real, working example already in this project

# Step 54's auth_state / authenticated_page fixtures in conftest.py are a genuine instance of this exact principle: instead of running the login UI flow (fill username, fill password, click login) at the start of every single test, the session is authenticated once, saved, and reused - every test that needs to be "logged in" starts there directly, skipping the slow, repeated UI setup entirely.

# In a job with a real backend, the same idea would extend further: e.g. seeding cart contents, creating test users, or setting account permissions via a direct API/database call instead of clicking through the UI to get there - the login shortcut here is one specific case of the same general principle.
