from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from properties.serializer import PropertySerializer
# Create your views here.
class PropertyView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = PropertySerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        property_name = serializer.data
        return Response({"message":property_name})