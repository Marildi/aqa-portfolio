import os


def test_secret_key_is_available():
    secret = os.environ.get("SECRET_KEY")
    assert secret is not None
    assert len(secret) > 0
