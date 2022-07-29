from django.contrib import admin

# Register your models here.
from apps.projects.models import Project

admin.site.register(Project)
