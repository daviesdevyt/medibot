import uuid
from rest_framework import serializers


class PromptRequestSerializer(serializers.Serializer):
    prompt = serializers.CharField(write_only=True)
    session_id = serializers.CharField(write_only=True, default=uuid.uuid4)
