from rest_framework import serializers

from notion.models import Page
from utils.fields import NotionField
from utils.fields import PageField


class PageSerializer(serializers.ModelSerializer):
    notion = NotionField(allow_null=True, required=False)
    parent = PageField()

    class Meta:
        model = Page
        fields = (
            "id",
            "name",
            "external_id",
            "notion",
            "parent"
        )
