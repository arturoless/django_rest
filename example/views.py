from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from example.models import Example
from example.forms import ImageUploadForm, PersonUploadForm, CareerUploadForm

from example.models import Imagen

from example.models import Person

from example.models import Career

from example.serializer import ExampleSerializers, PersonSerializers, CareerSerializers

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
    def post(self, request):
        form = PersonUploadForm(request.data, request.FILES)
        if form.is_valid():
            form.save()
            return Response('ok')
        return Response('nok')

class PersonView(APIView):

    
    
    def put(self, request, id, format=None):
        person_id = int(id)
        try:
            person = Person.objects.get(id = person_id)
        except ObjectDoesNotExist:
           return Response('does not exist')
        form = PersonUploadForm(request.data, instance = person)
        if form.is_valid():
            form.save()
            return Response('ok')
        return Response('nok')
    def get(self, request,id):
        try:
            return Response(PersonSerializers(Person.objects.get(pk=id)).data)
        except Person.DoesNotExist:
            return Response('nok')

    def delete(self, request,id):
        person_id = int(id)
        try:
            person_sel = Person.objects.get(id = person_id)
        except Person.DoesNotExist:
            return Response('nok')
        person_sel.delete()
        return Response('ok')

class CareerList(APIView):
    def get(self, request):
        careers = Career.objects.all()
        serializer = CareerSerializers(careers, many=True)
        return Response(serializer.data)
    def post(self, request):
        form = CareerUploadForm(request.data, request.FILES)
        if form.is_valid():
            form.save()
            return Response('ok')
        return Response('nok')

class CareerView(APIView):

    
    def put(self, request, id):
        career_id = int(id)
        try:
            career = Career.objects.get(id = career_id)
        except ObjectDoesNotExist:
           return Response('nok')
        form = CareerUploadForm(request.data, instance = career)
        if form.is_valid():
            form.save()
            return Response(CareerSerializers(Career.objects.get(pk=id)).data)
        return Response('nok')
    def get(self, request,id):
        try:
            return Response(CareerSerializers(Career.objects.get(pk=id)).data)
        except Career.DoesNotExist:
            return Response('nok')

    def delete(self, request,id):
        career_id = int(id)
        try:
            career_sel = Career.objects.get(id = career_id)
        except Career.DoesNotExist:
            return Response('nok')
        career_sel.delete()
        return Response('ok')