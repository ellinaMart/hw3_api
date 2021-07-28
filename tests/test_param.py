import requests


def test_url_status(base_url4, resp_status_code):
    response = requests.get(base_url4)
    assert response.status_code == int(resp_status_code)