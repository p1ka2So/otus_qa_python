import pytest


def test_all_breweries_list(api_client):
    """ Checking all breweries list. """

    res = api_client.get(path='/breweries').json()
    for brewery in res:
        assert brewery['brewery_type'] in ('micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract',
                                           'proprietor')


@pytest.mark.parametrize('state', ['new_york', 'asdasd'])
def test_filter_by_state(api_client, state):
    """ Checking filter by state. """

    res = api_client.get(path='/breweries?by_state=' + state).json()
    if state == 'new_york':
        assert len(res) > 0
    else:
        assert len(res) == 0


@pytest.mark.parametrize('name', ['cooper', 'wasd'])
def test_filter_by_name(api_client, name):
    """ Checking filter by name. """

    res = api_client.get(path='/breweries?by_name=' + name).json()
    if name == 'cooper':
        assert len(res) > 0
    else:
        assert len(res) == 0


@pytest.mark.parametrize('brewery_id', [5494, 299])
def test_get_by_id(api_client, brewery_id):
    """ Checking brewery by ID. """

    res = api_client.get(path='/breweries/' + str(brewery_id)).json()
    assert len(res) == 14, "There should be 14 properties."
    assert res['id'] == brewery_id


def test_search_autocomplete(api_client):
    """ Checking search autocomplete. """

    res = api_client.get(path='/breweries/autocomplete?query=dog').json()
    for brewery in res:
        assert len(brewery) == 2
        assert isinstance(int(brewery['id']), int)
        assert 'dog' in brewery['name'].lower()

# TODO: Search function currently doesn't work, test fails.
# def test_search(api_client):
#
#     """ Checking search. """
#
#     res = api_client.get(path='/breweries/search?query=dog').json()
#     for brewery in res:
#         assert 'dog' in brewery['name'].lower()
#         assert len(brewery) == 14
#         assert isinstance(brewery['tag_list'], list)
