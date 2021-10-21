from fastapi import FastAPI
from fastapi.testclient import TestClient # uses pytest

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


# has requests API
client = TestClient(app)


def test_read_main():
    """
    pytest naming convention, test_fn_name

    client and function calls use pytest and must be *synchronous* 
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "msg" in response.json().keys()

