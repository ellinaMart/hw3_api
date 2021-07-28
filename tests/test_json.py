import requests
import pytest
from testdata.testdata import test_data


def test_api(base_url3):
    resp = requests.get(base_url3)
    global count_before
    assert resp.status_code == 200

@pytest.mark.parametrize('data_params', test_data, ids=[repr(x) for x in test_data])
def test_post(base_url3, data_params):
    resp = requests.post(base_url3, json=data_params)
    assert resp.status_code == 201

@pytest.mark.parametrize('userId', [1,2])
def test_filter(base_url3, userId):
    resp = requests.get(base_url3, params={'userId': userId})
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert resp.json()[i]['userId'] == userId

@pytest.mark.parametrize('data_test', test_data)
def test_put(base_url3, data_test):
    data_test['id'] = 101
    resp = requests.put(base_url3 + '/1', json=data_test)
    assert resp.status_code == 200

def test_comm(base_url3):
    resp = requests.get(base_url3 + '/1/comments')
    assert resp.status_code == 200
    for i in range(len(resp.json())):
        assert resp.json()[i]['postId'] == 1

