from django.db import models


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
    external_id = models.UUIDField()
