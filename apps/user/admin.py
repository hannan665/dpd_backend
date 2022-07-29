from django.contrib import admin

from apps.user.models import User
from apps.user.models import UserProfile
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
