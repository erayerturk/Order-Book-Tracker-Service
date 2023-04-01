
from pytest_mock import MockerFixture
import pytest

from order_book_tracker.order_book.factories import OrderBookFactory
from order_book_tracker.order_book.models import OrderBook, PeriodType, OrderBookStatistics
from order_book_tracker.order_book.tasks import get_and_save_order_book_data, update_or_create_statistics

pytestmark = pytest.mark.django_db


def test_get_order_book_data(mocker: MockerFixture):
    success_mock_response = mocker.Mock( **{"json.return_value": {
    "status": "success",
    "data": {
        "market_code": "BTCTRY",
        "ticker": {
            "market": {
                "market_code": "BTCTRY",
                "base_currency_code": "BTC",
                "counter_currency_code": "TRY"
            },
            "bid": "556861.14",
            "ask": "557473.00",
            "last_price": "557349.63",
            "last_size": "0.01308521",
            "volume_24h": "175.99",
            "change_24h": "0.07",
            "low_24h": "550000.00",
            "high_24h": "563936.97",
            "avg_24h": "557408.77",
            "timestamp": "1680356732.3938107"
            },
        },
    }})
    mocker.patch("order_book_tracker.order_book.tasks.requests.get", return_value=success_mock_response)
    get_and_save_order_book_data()
    assert OrderBook.objects.count() == 1


def calculate_statistics():
    OrderBookFactory.create(period_type=PeriodType.DAILY)
    OrderBookFactory.create(period_type=PeriodType.WEEKLY)
    OrderBookFactory.create(period_type=PeriodType.MONTHLY)
    assert OrderBookStatistics.objects.count() == 0
    update_or_create_statistics()
    assert OrderBookStatistics.objects.count() == 3

    # Check update
    update_or_create_statistics()
    assert OrderBookStatistics.objects.count() == 3
