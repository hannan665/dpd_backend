# Generated by Django 4.0.6 on 2022-07-23 13:34
import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=556, null=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('type', models.CharField(blank=True, max_length=556, null=True)),
                ('color', models.CharField(blank=True, default='#000', max_length=20, null=True)),
                ('key', models.CharField(default='NN', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
