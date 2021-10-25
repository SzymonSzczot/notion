from rest_framework import serializers

from notion.models import Page
from notion.serializers.page import PageSerializer
from notion.services.page import CreatePage


class CreatePageSerializer(serializers.Serializer):
    name = serializers.CharField()
    parent = serializers.CharField()

    def create(self, validated_data):
        parent = Page.objects.get(external_id=validated_data["parent"])
        page_service = CreatePage(validated_data["name"], parent)
        notion_page = page_service.create_page_in_notion(validated_data["name"])
        return page_service.create_page_instance(notion_page["id"], serializer_class=PageSerializer)
