from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY
from .serializers import PromptRequestSerializer
from .models import Session


# Create your views here.
class PromptRequestView(GenericAPIView):
    serializer_class = PromptRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prompt = serializer.validated_data.get("prompt")
        session_id = serializer.validated_data.get("session_id")

        session, created = Session.objects.get_or_create(session_id=session_id)
        session.messages.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4", messages=session.messages
        )

        openai_response = response["choices"][0]["message"]
        session.messages.append(openai_response)
        session.save()
        return Response(
            {"session_id": session.session_id, "content": openai_response["content"]}
        )


class MessagesView(GenericAPIView):

    def get(self, request, session_id, *args, **kwargs):
        session = get_object_or_404(Session, session_id=session_id)
        return Response(session.messages)
