# Generated by Django 2.1.14 on 2019-11-25 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0007_career'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='person',
            name='delete',
        ),
    ]