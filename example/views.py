from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from example.models import Example
from example.forms import ImageUploadForm

from example.models import Imagen

from example.serializer import ExampleSerializers

class ExampleList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        queryset = Example.objects.filter(delete = False)
        serializer = ExampleSerializers(queryset)
        return Response(serializer.data)

class ImagenList(APIView):
    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response('image upload success')
        return Response('allowed only via POST')
# Create your views here.
