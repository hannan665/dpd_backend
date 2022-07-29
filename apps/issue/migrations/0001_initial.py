# Generated by Django 4.0.6 on 2022-07-23 13:34
import uuid

import ckeditor.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment_text', ckeditor.fields.RichTextField(blank=True, verbose_name='comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=252, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('question_or_update', models.TextField(blank=True, null=True, verbose_name='Question or Updates')),
                ('is_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=252, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo')),
            ],
        ),
    ]
