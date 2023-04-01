import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from order_book_tracker.order_book.factories import OrderBookStatisticsFactory
from order_book_tracker.order_book.models import PeriodType

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.mark.parametrize(
    "period_type", [PeriodType.DAILY, PeriodType.WEEKLY, PeriodType.MONTHLY]
)
def test_order_book_statistics_api(period_type: PeriodType, api_client: APIClient):
    url = reverse("order-book-statistics", args=[period_type.label])
    OrderBookStatisticsFactory.create_batch(5, period_type=period_type)
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["count"] == 5
