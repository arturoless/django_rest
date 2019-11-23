from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from example.models import Example
from example.forms import ImageUploadForm, PersonUploadForm

from example.models import Imagen

from example.models import Person

from example.serializer import ExampleSerializers, PersonSerializers

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
# Create youviewr views here.
class PersonList(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializers(persons, many=True)
        return Response(serializer.data)

class PersonView(APIView):

    def post(self, request):
        form = PersonUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response('person save')
        return Response('person does not save')
    
    def put(self, request, id):
        person_id = int(id)
        try:
            person = Person.objects.get(id = person_id)
        except ObjectDoesNotExist:
           return Response('person does not exist')
        form = PersonUploadForm(request.POST, instance = person)
        if form.is_valid():
            form.save()
            return Response('person updated')
        return Response('something is wrong')
    def get(self, request,id):
        try:
            return Response(PersonSerializers(Person.objects.get(pk=id)).data)
        except Person.DoesNotExist:
            return Response('person does not exist')

    def delete(self, request,id):
        person_id = int(id)
        try:
            person_sel = Person.objects.get(id = person_id)
        except Person.DoesNotExist:
            return Response('person does not exist')
        person_sel.delete()
        return Response('person deleted')