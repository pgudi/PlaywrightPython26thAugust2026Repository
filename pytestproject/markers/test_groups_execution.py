import pytest

@pytest.mark.sanity
def test_sanity_testcase01():
    print("It is a First Sanity Testcase")

@pytest.mark.sanity
def test_sanity_testcase02():
    print("It is a Second Sanity Testcase")

@pytest.mark.regression
def test_regression_testcase01():
    print("It is a First Regression Testcase")

@pytest.mark.regression
def test_regression_testcase02():
    print("It is a Second Regression Testcase")

@pytest.mark.api
def test_api_testcase01():
    print("It is a First API Testcase")

@pytest.mark.api
def test_api_testcase02():
    print("It is a Second API Testcase")

@pytest.mark.database
def test_database_testcase01():
    print("It is a First Database Testcase")

@pytest.mark.database
def test_database_testcase02():
    print("It is a Second Database Testcase")
