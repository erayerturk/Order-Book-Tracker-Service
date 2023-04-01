from datetime import datetime, timedelta

from django.utils import timezone

from order_book_tracker.order_book.models import PeriodType


def get_start_date(period_type: int) -> datetime:
    """
    Calculates start date according to related period type

    :param period_type: Enum field of PeriodType class
    :return: datetime obj
    """
    now = timezone.now()
    if period_type == PeriodType.DAILY:
        start_date = now.replace(hour=0, minute=0, second=0)
    elif period_type == PeriodType.WEEKLY:
        week_day = now.isoweekday()
        start_week_date = now - timedelta(days=week_day - 1)
        start_date = start_week_date.replace(hour=0, minute=0, second=0)
    else:
        start_date = now.replace(day=1, hour=0, minute=0, second=0)
    return start_date



