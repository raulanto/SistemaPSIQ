# Generated by Django 5.0.6 on 2024-05-12 21:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_alter_persona_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='trabajador',
            unique_together={('pk_trabajador_curp', 'usuario')},
        ),
    ]