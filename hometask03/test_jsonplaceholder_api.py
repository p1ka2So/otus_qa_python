import random

import pytest


def test_get_posts_by_post_id(api_client):
    """ Get posts by post ID. """

    res = api_client.get(path='/comments?postId=1').json()
    print(res)
    for post in res:
        assert len(post) == 5
        assert post['postId'] == 1


def test_get_posts_by_user_id(api_client):
    """ Get posts by user ID. """

    res = api_client.get(path='/posts?userId=1').json()
    print(res)
    for post in res:
        assert len(post) == 4
        assert post['userId'] == 1


@pytest.mark.parametrize('input_id, output_id',
                         [(10, '10'), (1, '1')])
@pytest.mark.parametrize('input_title, output_title',
                         [('asd', 'asd'), ('123456', '123456')])
def test_post_request(api_client, input_id, output_id, input_title, output_title):
    """ Checking POST request. """

    res = api_client.post(
        path="/posts",
        data={'title': input_title,
              'body': 'bar',
              'userId': input_id}
    ).json()
    assert res['title'] == output_title
    assert res['body'] == 'bar'
    assert res['userId'] == output_id


@pytest.mark.parametrize('user_id', [-1, 0])
def test_negative_filtering(api_client, user_id):
    """ Nothing returned if user ID is 0 or -1. """

    res = api_client.get(
        path="/posts",
        params={'userId': user_id}
    ).json()
    assert len(res) == 0


@pytest.mark.parametrize('user_id, user_id_in_response', [(1, 1), (2, 2)])
def test_api_filtering(api_client, user_id, user_id_in_response):
    """ Checking userId of random post. """

    res = api_client.get(
        path="/posts",
        params={'userId': user_id}
    ).json()
    random_post_number = random.randint(1, 10)
    assert res[random_post_number]['userId'] == user_id_in_response
