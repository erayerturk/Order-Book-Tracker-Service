import time
from datetime import datetime

import pytz
from rest_framework import serializers


class UnixEpochDatetimeField(serializers.DateTimeField):
    def to_representation(self, value):
        if not value:
            return None
        value = self.enforce_timezone(value)
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        return datetime.fromtimestamp(float(value), tz=pytz.UTC)
