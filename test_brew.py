import cerberus
import requests
import pytest

@pytest.mark.parametrize('city', ['San Diego', 'Alameda'])
def test_api(base_url2, city):
    resp = requests.get(base_url2, data={'by_city': city}
                        )
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert resp.json()[i]['city'] == city



    # v = cerberus.Validator()
    # assert v.validate(resp.json(), schema)