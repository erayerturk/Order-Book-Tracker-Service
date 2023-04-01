from django.db.models import Avg, Max, Min, Sum

from order_book_tracker.order_book.models import OrderBook, OrderBookStatistics
from order_book_tracker.utils.date_utils import get_start_date


def calculate_statistics(period_type: int):
    """
    Calculate order book statistics

    :param period_type: Daily: 0, Weekly: 1, Monthly: 2
    :return:
    """
    start_date = get_start_date(period_type)
    result = OrderBook.objects.filter(timestamp__gte=start_date).aggregate(
        min_price=Min("last_price"),
        max_price=Max("last_price"),
        avg_price=Avg("last_price"),
        total_volume=Sum("last_size"),
    )

    try:
        statistic = OrderBookStatistics.objects.filter(
            created_at__gte=start_date, period_type=period_type
        ).first()
        statistic.min_price = result.get("min_price")
        statistic.max_price = result.get("max_price")
        statistic.average_price = result.get("avg_price")
        statistic.total_volume = result.get("total_volume")
        statistic.save()
    except AttributeError:
        OrderBookStatistics.objects.create(
            period_type=period_type,
            min_price=result.get("min_price"),
            max_price=result.get("max_price"),
            average_price=result.get("avg_price"),
            total_volume=result.get("total_volume"),
        )
