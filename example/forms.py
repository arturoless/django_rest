from django import forms

from example.models import Person, Imagen,Career
class ImageUploadForm(forms.ModelForm):
     class Meta:
        model = Imagen
        fields = ('model_pic1', 'model_pic2', 'model_pic3',)
class PersonUploadForm(forms.ModelForm):
     class Meta:
        model = Person
        fields = ('name', 'lastname', 'age','address','career')
class CareerUploadForm(forms.ModelForm):
     class Meta:
        model = Career
        fields = ('name', 'slug')