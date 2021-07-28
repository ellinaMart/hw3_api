import requests
import pytest


testdata = [('cooper','Cooper'),
            ('modern%20times', 'Modern Times Barrel House')]

def test_api(base_url2):
    resp = requests.get(base_url2)
    assert resp.status_code == 200

@pytest.mark.parametrize('city', ['San Diego', 'Alameda'])
def test_api_city(base_url2, city):
    resp = requests.get(base_url2, params={'by_city': city})
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert resp.json()[i]['city'] == city

@pytest.mark.parametrize('name, expected', testdata)
def test_api_name(base_url2, name, expected):
    resp = requests.get(base_url2, params={'by_name': name})
    assert resp.status_code == 200

@pytest.mark.parametrize('state', ['Ohio','New York','New Mexico'])
def test_api_state(base_url2, state):
    resp = requests.get(base_url2, params={'by_state': state})
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert resp.json()[i]['state'] == state

@pytest.mark.parametrize('postal', ['44107', '44107-4020'])
def test_api_postal(base_url2, postal):
    resp = requests.get(base_url2, params={'by_postal': postal})
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert postal in resp.json()[i]['postal_code']

