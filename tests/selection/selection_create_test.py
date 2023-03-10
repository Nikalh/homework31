import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, access_token):
    ad_list = AdFactory.create_batch(3)

    data = {
        "name": "Моя подборка",
        "owner": "test",
        "items": [ad.pk for ad in ad_list]
    }
    expected_data = {
        "id": 1,
        "name": "Моя подборка",
        "owner": "test",
        "items": [ad.pk for ad in ad_list]
    }
    response = client.post("/selection/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
