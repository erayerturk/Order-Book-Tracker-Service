from django.db import models
from django.utils import timezone


class PeriodType(models.IntegerChoices):
    DAILY = 0, 'daily'
    WEEKLY = 1, 'weekly'
    MONTHLY = 2, 'monthly'


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderBook(TimeStampedModel):
    market_code = models.CharField(max_length=10)
    last_price = models.FloatField()
    last_size = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)


class OrderBookStatistics(TimeStampedModel):
    period_type = models.IntegerField(default=PeriodType.DAILY, choices=PeriodType.choices)
    min_price = models.FloatField()
    max_price = models.FloatField()
    average_price = models.FloatField()
    total_volume = models.FloatField()
