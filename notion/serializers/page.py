from rest_framework import serializers

from notion.models import Page
from utils.fields import NotionField


class PageSerializer(serializers.ModelSerializer):
    notion_id = NotionField()

    class Meta:
        model = Page
        fields = (
            "name",
            "external_id",
            "notion_id"
        )
