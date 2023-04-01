from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny

from order_book_tracker.order_book.models import OrderBookStatistics, PeriodType
from order_book_tracker.order_book.serializers import OrderBookStatisticsSerializer


class OrderBookStatisticsAPIView(generics.ListAPIView):
    http_method_names = ["get"]
    serializer_class = OrderBookStatisticsSerializer
    authentication_classes = ()
    permission_classes = (AllowAny,)
    ordering = ("-created_at",)

    def get_queryset(self):
        period_type = self.kwargs["period_type"]
        if period_type in PeriodType.labels:
            return OrderBookStatistics.objects.filter(
                period_type=PeriodType.labels.index(period_type)
            )
        raise ValidationError(
            f"Not valid period type. Valid options: {PeriodType.labels}"
        )
