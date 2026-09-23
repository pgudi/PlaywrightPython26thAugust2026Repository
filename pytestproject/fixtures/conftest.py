import pytest

@pytest.fixture(scope="function")
def setup():
    print("Launch Chromium Browser and Navigate URL and Login with Application")
    yield
    print("Logout from Application and Close Chromium Browser")

@pytest.fixture(scope="class")
def setup_class():
    print("Launch Chromium Browser and Navigate URL and Login with Application - Class Level")
    yield
    print("Logout from Application and Close Chromium Browser - Class Level")

@pytest.fixture(scope="module")
def setup_module():
    print("Launch Chromium Browser and Navigate URL and Login with Application - Module Level")
    yield
    print("Logout from Application and Close Chromium Browser - Module Level")