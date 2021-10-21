from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from notion.views import PageViewSet

router = DefaultRouter(trailing_slash=False)
router.register("pages", PageViewSet, basename="pages")

urlpatterns = [
    path("", include(router.urls)),
]
