from pytest import fail
from werkzeug.exceptions import NotFound

import requests

base_url = "http://127.0.0.1:5000/news/"
headers = {
    "accept": "*/*",
    'User-Agent': 'request'
}


def test_get_all_news_route_exists():
    data = requests.get(base_url, headers=headers)
    answer = requests.get(base_url, headers=headers)
    assert answer.status_code == 200


def test_post_news():
    post_url = base_url+'/create'
    data = {
        "title": "Titulo exemplo",
        "subtitle": "Author",
        "content": "Descrição muita longa aqui...",
        "upvotes": 1,
        "downvotes": 1,
        "approved": "True",
        "news_category": 1
    }
    answer = requests.post(post_url, json=data, headers=headers)
    assert answer.status_code == 200
