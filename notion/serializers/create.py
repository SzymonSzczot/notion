from rest_framework import serializers

from notion.serializers.page import PageSerializer
from notion.services.page import CreatePage


class CreatePageSerializer(serializers.Serializer):
    name = serializers.CharField()
    parent = PageSerializer()
    properties = serializers.JSONField()

    def create(self, validated_data):
        page_service = CreatePage(validated_data["name"], validated_data["parent"])
        notion_page = page_service.create_page_in_notion(validated_data["properties"])
        return page_service.create_page_instance(notion_page["id"], serializer_class=PageSerializer)
