import pytest

from ads.serializers.ad import AdSerializer
from tests.factories.ad import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ads = AdFactory.create_batch(10)

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == AdSerializer(ads, many=True).data