# Generated by Django 3.0.14 on 2022-02-24 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20220218_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
    ]
