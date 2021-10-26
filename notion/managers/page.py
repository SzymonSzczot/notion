from django.db.models import Manager

from notion.services import CreatePropertiesService


class PageManager(Manager):

    def create(self, **kwargs):
        properties = kwargs.pop("properties")
        instance = super().create(**kwargs)
        properties_create_service = CreatePropertiesService(instance, properties)
        properties_create_service.create_properties()
        return instance
