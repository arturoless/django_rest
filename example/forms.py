from django import forms

from example.models import Imagen
class ImageUploadForm(forms.ModelForm):
     class Meta:
        model = Imagen
        fields = ('model_pic1', 'model_pic2', 'model_pic3',)