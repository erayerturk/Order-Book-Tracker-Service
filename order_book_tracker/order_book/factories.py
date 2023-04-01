from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice

from order_book_tracker.order_book.models import (
    OrderBook,
    OrderBookStatistics,
    PeriodType,
)


class OrderBookFactory(DjangoModelFactory):
    market_code = "BTCTRY"
    last_price = Faker("pyfloat", positive=True, max_value=60, right_digits=2)
    last_size = Faker("pyfloat", positive=True, max_value=10, right_digits=2)
    timestamp = Faker("timestamp")

    class Meta:
        model = OrderBook


class OrderBookStatisticsFactory(DjangoModelFactory):
    period_type = FuzzyChoice(PeriodType, getter=lambda v: v.value)
    min_price = Faker("pyfloat", positive=True, max_value=40, right_digits=2)
    max_price = Faker("pyfloat", positive=True, max_value=60, right_digits=2)
    average_price = Faker("pyfloat", positive=True, max_value=50, right_digits=2)
    total_volume = Faker("pyfloat", positive=True, max_value=60, right_digits=2)

    class Meta:
        model = OrderBookStatistics
