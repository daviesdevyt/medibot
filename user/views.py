from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
# Create your views here.

from rest_framework.response import Response

class SignupUserView(APIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"name": "John", "age": 23})