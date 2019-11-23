from django.db import models
from django.utils import timezone

class Example(models.Model):
    name = models.CharField(max_length=254, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Example'

class Example2(models.Model):
    name = models.CharField(max_length=254, null=False)
    year = models.IntegerField(null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Example2'

class Imagen(models.Model):
    model_pic1 = models.ImageField(upload_to = 'pic_folder/')
    model_pic2 = models.ImageField(upload_to = 'pic_folder/')
    model_pic3 = models.ImageField(upload_to = 'pic_folder/')
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Imagen'
        
class Person(models.Model):
    name = models.CharField(max_length=245)
    lastname = models.CharField(max_length=245)
    age = models.CharField(max_length=245)
    address = models.CharField(max_length=245)
    career = models.CharField(max_length=245)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Person'

