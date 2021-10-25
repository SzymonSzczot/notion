from rest_framework.fields import Field

from notion.models import Notion
from notion.models import Page


class TwoWayField(Field):
    klass = None

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class NotionField(TwoWayField):
    klass = Notion

    def to_representation(self, value):
        return str(value)


class PageField(TwoWayField):
    klass = Page

    def to_internal_value(self, data):
        return Page.objects.get(external_id=data)

    def to_representation(self, value):
        return value.get_details()
