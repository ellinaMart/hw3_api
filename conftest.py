import pytest
import requests

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
    parser.addoption(
        "--url3",
        action="store",
        default="https://jsonplaceholder.typicode.com/posts",
        help="This is request url"
    )
    parser.addoption(
        "--url4",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default='200',
        choices = ['200', '300', '400', '404', '500', '502'],
        help="This is status code"
    )

@pytest.fixture(scope="session")
def base_url1(request):
    return request.config.getoption("--url1")

@pytest.fixture(scope="session")
def base_url2(request):
    return request.config.getoption("--url2")

@pytest.fixture(scope="session")
def base_url3(request):
    return request.config.getoption("--url3")

@pytest.fixture(scope="session")
def base_url4(request):
    return request.config.getoption("--url4")

@pytest.fixture(scope="session")
def resp_status_code(request):
    return request.config.getoption("--status_code")

