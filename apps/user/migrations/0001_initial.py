# Generated by Django 4.0.6 on 2022-07-23 13:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('_photo_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Photo url')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('photo_base64', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, default='', max_length=250, verbose_name='About')),
                ('team_count', models.PositiveIntegerField(default='0', verbose_name='Follower count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('is_account_setup', models.BooleanField(default=False, verbose_name='Is account setup?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin?')),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted date')),
                ('created_by_google', models.BooleanField(default=False, verbose_name='Created by google account')),
                ('created_by_facebook', models.BooleanField(default=False, verbose_name='Created by facebook account')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='user.userprofile')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
