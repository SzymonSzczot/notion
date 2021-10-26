from django.db import models

from notion.models.content_constants import ContentConstants


class Content(models.Model):

    property = models.ForeignKey(
        "notion.Property",
        on_delete=models.CASCADE,
        related_name="contents"
    )
    type = models.CharField(choices=ContentConstants.TYPE_CHOICES, default=ContentConstants.TEXT, max_length=30)
    value = models.CharField(max_length=200, default="")
    color = models.CharField(
        max_length=10,
        choices=ContentConstants.COLOR_CHOICES,
        default=ContentConstants.DEFAULT
    )

    def for_property(self):
        return {
            **self.additional_fields(),
            self.type: self.get_content()
        }

    def additional_fields(self):
        if self.type == ContentConstants.TEXT:
            return {"type": "text"}
        return dict()

    def get_content(self):
        if self.type == ContentConstants.TEXT:
            return {
                "content": self.value
            }
        if self.type == ContentConstants.NUMBER:
            return float(self.value)
