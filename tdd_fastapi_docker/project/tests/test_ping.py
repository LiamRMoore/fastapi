

def test_ping(test_app):
    # given
    # when
    response = test_app.get("/ping")
    # then
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev", "ping": "pong!", "testing": True
    }
