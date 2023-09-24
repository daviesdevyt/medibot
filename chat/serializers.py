from rest_framework import serializers


class PromptRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField(write_only=True)
