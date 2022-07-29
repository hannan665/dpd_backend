from django.contrib import admin

from apps.issue.models import Comment
from apps.issue.models import Issue
from apps.issue.models import IssueType
# Register your models here.

admin.site.register(IssueType)
admin.site.register(Issue)
admin.site.register(Comment)
