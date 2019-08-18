import json
import random
import re

import pytest


def test_all_breeds_list(api_client):
    """ Checking all breeds list. """

    res = api_client.get(path='/breeds/list/all').json()

    with open('.\\hometask03\\dog_api_data\\list_of_breeds.json', 'r') as f:
        assert res['message'] == json.load(f)
    assert res['status'] == 'success'


@pytest.mark.parametrize('breed', ['eskimo', 'hound/english'])
def test_random_breed_image(api_client, breed):
    """ Checking random breed images. """

    res = api_client.get(path='/breed/' + breed + '/images/random').json()
    # Too lazy to create normal URL building function for 1 lesson
    if '/' in breed:
        breed = breed.replace('/', '-')
    regex = re.compile('https://images.dog.ceo/breeds/' + breed + r'/n\d+?_\d+?' + '.jpg')
    assert re.match(regex, res['message']) is not None
    assert res['status'] == 'success'


@pytest.mark.parametrize('breed', ['eskimo', 'hound/english'])
def test_all_breed_images_list(api_client, breed):
    """ Checking array of all the images of a breed. """

    res = api_client.get(path='/breed/' + breed + '/images').json()
    # Too lazy to create normal URL building function for 1 lesson
    if '/' in breed:
        breed = breed.replace('/', '-')
    regex = re.compile('https://images.dog.ceo/breeds/' + breed + r'/n\d+?_\d+?' + '.jpg')
    assert len(res['message']) > 1, "Should be more than 1 image in result."
    for url in res['message']:
        assert re.match(regex, url) is not None
    assert res['status'] == 'success'


@pytest.mark.parametrize('breed', ['eskimo', 'hound/english'])
def test_random_breed_images_list(api_client, breed):
    """ Checking array of random images of a breed. """

    img_number = random.randint(1, 6)
    res = api_client.get(path='/breed/' + breed + '/images/random/' + str(img_number)).json()
    # Too lazy to create normal URL building function for 1 lesson
    if '/' in breed:
        breed = breed.replace('/', '-')
    regex = re.compile('https://images.dog.ceo/breeds/' + breed + r'/n\d+?_\d+?' + '.jpg')
    assert len(res['message']) == img_number, "Should be {} images in result.".format(img_number)
    for url in res['message']:
        assert re.match(regex, url) is not None
    assert res['status'] == 'success'


def test_sub_breeds_list(api_client):
    """ Checking an array of all the sub-breeds from a breed. """

    res = api_client.get(path='/breed/hound/list').json()
    assert isinstance(res['message'], list)
    for breed in res['message']:
        assert re.match('^[a-z]*$', breed)
    assert res['status'] == 'success'
