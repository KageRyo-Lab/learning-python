import pytest
from get import get_api
from post import post_api
from put import put_api
from delete import delete_api

def test_get_api():
    result = get_api()
    assert isinstance(result, dict)
    assert 'userId' in result
    assert 'id' in result
    assert 'title' in result
    assert 'body' in result
    assert isinstance(result['userId'], int)
    assert isinstance(result['id'], int)
    assert isinstance(result['title'], str)
    assert isinstance(result['body'], str)

def test_post_api():
    result = post_api()
    assert isinstance(result, dict)
    assert 'id' in result
    assert 'title' in result
    assert 'body' in result
    assert 'userId' in result
    assert result['title'] == "Today Weather"
    assert result['body'] == "HOOOOOOOOOOOT!"
    assert result['userId'] == 1

def test_put_api():
    result = put_api()
    assert isinstance(result, dict)
    assert 'id' in result
    assert 'title' in result
    assert 'body' in result
    assert 'userId' in result
    assert result['title'] == "Hambuger"
    assert result['body'] == "good"
    assert result['userId'] == 1
    assert result['id'] == 1

def test_delete_api():
    result = delete_api()
    assert isinstance(result, dict)
    assert len(result) == 0