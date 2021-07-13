import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url1",
        action="store",
        default="https://dog.ceo/api/",
        help="This is dog url"
    )
    parser.addoption(
        "--url2",
        action="store",
        default="https://api.openbrewerydb.org/breweries",
        help="This is request url"
    )

@pytest.fixture(scope="session")
def base_url1(request):
    return request.config.getoption("--url1")

@pytest.fixture(scope="session")
def base_url2(request):
    return request.config.getoption("--url2")