import base64
import uuid
from typing import Optional

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


def upload_to(instace, file_name):
    return '/'.join(['photo', instace.name])


class UserProfile(models.Model):
    """ User profile """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _photo_url = models.CharField(
        _("Photo url"),
        max_length=256,
        blank=True,
        null=True)
    name = models.CharField(_("Name"), max_length=256, blank=True)
    photo = models.ImageField(
        upload_to='photo',
        blank=True,
        null=True
    )
    photo_base64 = models.TextField(
        blank=True,
        null=True
    )
    about = models.TextField(_("About"), max_length=250, blank=True, default='')
    team_count = models.PositiveIntegerField(_("Follower count"), null=False, default='0')
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        # if self.name == None:
        #     return " NAME IS NULL"
        return self.name

    @property
    def uuid(self):
        return str(self.id)

    def get_FL_names(self):
        first, *last = self.name.split(' ')
        return first if first else "user", last[0] if last else ""

    @property
    def photo_url(self):
        if self._photo_url:
            return self._photo_url
        elif self.photo:
            return self.photo.url
        else:
            return None

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        if self.photo:
            img_file = open(self.photo.path, "rb")
            img = (base64.b64encode(img_file.read())).decode('UTF-8')
            self.photo_base64 = 'data:image/%s;base64,%s' % ('png', img)
            super(UserProfile, self).save(*args, **kwargs)


class CustomUserManager(BaseUserManager):

    def create_user(self,
                    email: str,
                    password: str,
                    group: Optional[Group] = None,
                    **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        if group is not None:
            group.user_set.add(user)

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        return user


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256, )
    is_account_setup = models.BooleanField(_("Is account setup?"), default=False)
    is_admin = models.BooleanField(_("Is admin?"), default=False)
    deleted_date = models.DateTimeField(
        _("Deleted date"), blank=True, null=True)
    created_by_google = models.BooleanField(
        _("Created by google account"), default=False)
    created_by_facebook = models.BooleanField(
        _("Created by facebook account"), default=False)

    profile = models.OneToOneField(
        "UserProfile",
        on_delete=models.CASCADE,
        blank=True,
        related_name='userprofile',
        null=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        app_label = 'user'

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        # if self.email == None:
        #     return " EMAIL IS NULL"
        return self.email
