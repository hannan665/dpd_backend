from django.contrib import admin

# Register your models here.
from apps.user.models import UserProfile, User

admin.site.register(User)
admin.site.register(UserProfile)
