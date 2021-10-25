import json

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from notion.connectors import NotionService
from notion.models import Notion
from notion.models import Page
from notion.serializers.create import CreatePageSerializer
from notion.serializers.page import PageSerializer
from notion.serializers.update import UpdatePageSerializer


class PageViewSet(viewsets.ModelViewSet):

    lookup_field = "external_id"
    queryset = Page.objects.all()

    page_serializer = PageSerializer
    create_serializer = CreatePageSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.page_serializer
        elif self.action == "create":
            return self.create_serializer
        return self.page_serializer

    def retrieve(self, request, *args, **kwargs):
        notion = Notion.objects.first()
        notion_connector = NotionService(notion)
        response = notion_connector.get_page_properties(self.get_object())
        return Response(json.loads(response.content))

    def create(self, request, *args, **kwargs):
        serializer = CreatePageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "created"}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = UpdatePageSerializer(data=request.data)
