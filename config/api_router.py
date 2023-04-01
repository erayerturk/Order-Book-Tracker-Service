from django.conf import settings
from django.urls import re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from order_book_tracker.users.api.views import UserViewSet
from order_book_tracker.order_book.views import OrderBookStatisticsAPIView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
