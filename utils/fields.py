from rest_framework.fields import Field

from notion.models import Notion


class TwoWayField(Field):
    klass = None

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class NotionField(TwoWayField):
    klass = Notion
