from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


# Create your views here.
class PromptRequestView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        response = openai.ChatCompletion.create(
            model="gpt-4", messages=request.data.get("messages")
        )
        return Response(response)
