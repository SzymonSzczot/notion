from django.db import models


class Notion(models.Model):
    service_url = models.URLField()
    internal_integration_token = models.CharField(max_length=300, default="")
    bearer_token = models.CharField(max_length=200, default="")
    version = models.CharField(max_length=30, default="2021-05-13")

    def __repr__(self):
        return f"<{self.id}: {self.service_url}"

    def __str__(self):
        return f"<{self.id}: {self.service_url}"