from django.contrib.gis.db import models

from notion.models.properties_constants import PropertyConstants


class Property(models.Model):
    page = models.ForeignKey(
        "notion.Page",
        on_delete=models.CASCADE,
        related_name="properties"
    )
    type = models.CharField(
        choices=PropertyConstants.TYPE_CHOICES,
        max_length=20,
        default=PropertyConstants.TITLE
    )
    name = models.CharField(max_length=40)

    def get_property(self):
        return {
            self.type: self.get_content()
        }

    def get_content(self):
        if self.contents.count() > 1:
            return [content.for_property() for content in self.contents.all()]
        if self.contents.exists():
            return self.contents.first().for_property()
        return dict()

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
