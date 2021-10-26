import requests

from notion.models import Notion
from notion.models import Page


class NotionService:
    def __init__(self, notion: Notion):
        self.notion = notion

    def get_auth_headers(self):
        return {
            "Authorization": f"Bearer {self.notion.bearer_token}",
            "Notion-Version": self.notion.version
        }

    def get_page_properties(self, page):
        url = f"{self.notion.service_url}/v1/pages/{page.external_id}"
        return requests.get(url, headers=self.get_auth_headers())

    def create_page(self, parent: Page, page: Page):
        url = f"{self.notion.service_url}/v1/pages"
        payload = {
            "parent": {
                "type": "page_id",
                "page_id": parent.external_id
            },
            "properties": page.get_properties()

        }
        return requests.post(url, json=payload, headers=self.get_auth_headers())
