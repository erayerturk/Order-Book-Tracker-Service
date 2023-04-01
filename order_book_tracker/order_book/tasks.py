import requests

from config import celery_app
from config.settings.base import BITEXEN_ORDER_BOOK_API_URL
from order_book_tracker.order_book.models import PeriodType
from order_book_tracker.order_book.serializers import OrderBookSerializer
from order_book_tracker.order_book.statistics import calculate_statistics


@celery_app.task
def get_and_save_order_book_data() -> None:
    """
    Collects order book data periodically

    :return:
    """
    url = BITEXEN_ORDER_BOOK_API_URL
    response = requests.get(url, timeout=5)
    if response.ok:
        data = response.json()["data"]["ticker"]
        data.pop("market")
        data["market_code"] = response.json()["data"]["market_code"]
        serializer = OrderBookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


@celery_app.task
def update_or_create_statistics() -> None:
    """
    Calculates order book statistics to create or update

    :return:
    """
    for period_type in PeriodType.values:
        calculate_statistics(period_type)
