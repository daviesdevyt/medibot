from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PromptRequestSerializer
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


# Create your views here.
class PromptRequestView(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PromptRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        pre = "Let's have a doctor - patient conversation\n"
        response = openai.Completion.create(
            model="text-davinci-003", prompt=pre + serializer.validated_data["prompt"]
        )
        return Response(response)
