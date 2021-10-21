import json

from notion.connectors import NotionService
from notion.models import Notion


class CreatePage:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def create_page_instance(self, external_id, serializer_class):
        page_serializer = serializer_class(data={**self.parent, "external_id": external_id})
        page_serializer.is_valid(raise_exception=True)
        return page_serializer.save()

    def create_page_in_notion(self, properties):
        notion_client = NotionService(Notion.objects.first())
        response = notion_client.create_page(parent=self.parent, properties=properties)
        response_content = json.loads(response.content)
        assert response.status_code == 200, response_content
        return response_content
