import cerberus
import requests

def test_api(base_url):
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"},
    }
    resp = requests.get(base_url + "breeds/image/random")
    assert resp.status_code == 200
    assert resp.json()['status'] == 'success'
    v = cerberus.Validator()
    assert v.validate(resp.json(), schema)

def test_breads_list(base_url):
    resp = requests.get(base_url + "breeds/list/all")
    assert resp.status_code == 200

def test_bread_from_list(base_url):
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"},
    }
    resp = requests.get(base_url + "breed/hound/images")
    assert resp.status_code == 200
    v = cerberus.Validator()
    assert v.validate(resp.json(), schema)

def test_sub_bread(base_url):
    schema = {
        "message": {"type": "list"},
        "status": {"type": "string"},
    }
    resp = requests.get(base_url + "breed/hound/afghan/images")
    assert resp.status_code == 200
    v = cerberus.Validator()
    assert v.validate(resp.json(), schema)

def test_sub_bread_image(base_url):
    schema = {
        "message": {"type": "string"},
        "status": {"type": "string"},
    }
    resp = requests.get(base_url + "breed/hound/afghan/images/random")
    assert resp.status_code == 200
    v = cerberus.Validator()
    assert v.validate(resp.json(), schema)