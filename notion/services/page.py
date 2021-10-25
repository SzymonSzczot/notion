import json

from notion.connectors import NotionService
from notion.models import Notion
from notion.models import Page


class CreatePage:

    def __init__(self, name, parent: Page = None):
        self.name = name
        self.parent = parent

    def create_page_instance(self, external_id, serializer_class):
        page_serializer = serializer_class(data={
            "notion": self.get_notion_instance(),
            "name": self.name,
            "external_id": external_id,
            "parent": self.parent
        })
        page_serializer.is_valid(raise_exception=True)
        return page_serializer.save()

    def get_notion_instance(self):
        return Notion.objects.first()

    def create_page_in_notion(self, name):
        notion_client = NotionService(Notion.objects.first())
        response = notion_client.create_page(parent_id=self.parent.external_id, title=name)
        response_content = json.loads(response.content)
        assert response.status_code == 200, response_content
        return response_content
