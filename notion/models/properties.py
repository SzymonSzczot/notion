from django.db import models

from notion.serializers.properties.rich_text import PropertyRichTextSerializer


class Property(models.Model):

    TITLE = "title"
    RICH_TEXT = "rich_text"

    TYPE_CHOICES = (
        (TITLE, "title"),
        (RICH_TEXT, "rich_text")
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)

    def get_property(self):
        return PropertyRichTextSerializer({
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Jakiś tekst"
                    }
                }
            ]
        })
