# Generated by Django 5.0.6 on 2024-05-11 21:38

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='', upload_to='foto/'),
        ),
    ]
