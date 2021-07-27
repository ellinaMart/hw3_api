import requests
import pytest
from testdata.testdata import test_data


def test_api(base_url3):
    resp = requests.get(base_url3)
    #import pdb; pdb.set_trace()
    #global count
    count = len(resp.json())
    assert resp.status_code == 200

@pytest.mark.parametrize('data_params', test_data, ids=[repr(x) for x in test_data])
#@pytest.mark.parametrize('data_params', test_data)
def test_post(base_url3, data_params):
    resp = requests.post(base_url3, json=data_params)
    assert resp.status_code == 201

data = test_data[0]
@pytest.mark.parametrize('data_params', data)
def test_put(base_url3, data_params):
    print(test_data)
    test_data[0]['id'] = 101
    import pdb; pdb.set_trace()
    resp = requests.put(base_url3, json=data_params)
    import pdb; pdb.set_trace()
    assert resp.status_code == 201


