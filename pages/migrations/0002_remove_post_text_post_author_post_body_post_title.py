# Generated by Django 4.1.13 on 2023-12-24 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
