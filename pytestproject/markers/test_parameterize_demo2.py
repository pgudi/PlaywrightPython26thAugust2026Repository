import pytest

@pytest.mark.parametrize(
    "username, password",
    [("santosh","India123"),("Srinu","Welcome123"), ("Vinu", "Password@123")]
)

def test_login_params(username, password):
    print(username, " --> ",password)