from django import forms

from example.models import Person, Imagen
class ImageUploadForm(forms.ModelForm):
     class Meta:
        model = Imagen
        fields = ('model_pic1', 'model_pic2', 'model_pic3',)
class PersonUploadForm(forms.ModelForm):
     class Meta:
        model = Person
        fields = ('name', 'lastname', 'age','address','career')