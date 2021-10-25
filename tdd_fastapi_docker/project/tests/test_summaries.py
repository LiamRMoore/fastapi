import json


# -- create summary

def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"})
    )
    assert response.status_code == 201
    response_dict = response.json()
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["id"]


def test_create_summaries_invalid_json(test_app):
    response = test_app.post("/summaries/", data=json.dumps({"bla": "blu"}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


# -- read single summary

def test_read_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_non_existing_summary(test_app_with_db):
    response = test_app_with_db.get("/summaries/666")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


# -- get all summaries

def test_read_all_summaries(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(
        lambda d: d["id"] == summary_id, response_list
    ))) == 1
