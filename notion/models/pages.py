from django.db import models

from notion.managers.page import PageManager


class Page(models.Model):
    notion = models.ForeignKey(
        "notion.Notion",
        on_delete=models.CASCADE,
        related_name="pages"
    )
    parent = models.ForeignKey(
        "notion.Page",
        on_delete=models.CASCADE,
        null=True,
        related_name="children"
    )
    name = models.CharField(max_length=100)
    external_id = models.CharField(max_length=100)

    objects = PageManager()

    def get_details(self):
        return {
            "parent": self.get_parent_details(),
            "name": self.name,
            "external_id": self.external_id
        }

    def get_parent_details(self):
        if self.parent:
            return self.parent.get_details()

    def get_properties(self):
        return {
            page_property.name: page_property.get_property()
            for page_property in self.properties.all()
        }

    def __str__(self):
        return f"{self.external_id}"
