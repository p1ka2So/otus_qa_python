def test_ya_ru_get_200(api_client):
    """ Get 200 from https://ya.ru. """

    assert api_client.get().status_code == 200
