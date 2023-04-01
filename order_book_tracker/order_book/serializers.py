from rest_framework import serializers

from order_book_tracker.order_book.models import (
    OrderBook,
    OrderBookStatistics,
    PeriodType,
)
from order_book_tracker.utils.fields import UnixEpochDatetimeField


class OrderBookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    market_code = serializers.CharField(max_length=10)
    last_price = serializers.FloatField()
    last_size = serializers.FloatField()
    timestamp = UnixEpochDatetimeField()

    class Meta:
        model = OrderBook
        fields = ("market_code", "last_price", "last_size", "timestamp")
        read_only_fields = (
            "id",
            "timestamp",
        )

    def create(self, validated_data):
        return OrderBook.objects.create(**validated_data)


class OrderBookStatisticsSerializer(serializers.Serializer):
    period_type = serializers.IntegerField()
    min_price = serializers.FloatField()
    max_price = serializers.FloatField()
    average_price = serializers.FloatField()
    total_volume = serializers.FloatField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = OrderBookStatistics
        fields = (
            "period_type",
            "min_price",
            "max_price",
            "average_price",
            "total_volume",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at",)

    def to_representation(self, instance):
        week = instance.created_at.isocalendar().week
        data = super().to_representation(instance)
        if data["period_type"] == PeriodType.WEEKLY:
            data["week"] = week
        data["period_type"] = PeriodType(data["period_type"]).label
        return data
