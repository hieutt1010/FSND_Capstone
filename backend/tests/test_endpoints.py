def test_get_actors_success():
    res = client.get('/actors')
    assert res.status_code == 200

def test_get_actors_error():
    res = client.get('/nonexistent')
    assert res.status_code == 404
