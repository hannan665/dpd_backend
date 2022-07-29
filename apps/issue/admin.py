from django.contrib import admin

# Register your models here.
from apps.issue.models import Comment, Issue, IssueType

admin.site.register(IssueType)
admin.site.register(Issue)
admin.site.register(Comment)
