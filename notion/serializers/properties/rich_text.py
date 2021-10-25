from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    content = serializers.CharField()


class RichTextSerializer(serializers.Serializer):
    type = serializers.CharField(default="text")
    text = TextSerializer()


class PropertyRichTextSerializer(serializers.Serializer):
    rich_text = RichTextSerializer(many=True)
