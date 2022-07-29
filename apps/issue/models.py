import uuid as uuid

from ckeditor.fields import RichTextField
from django.db import models

from django.utils.translation import gettext as _


class IssueType(models.Model):
    name = models.CharField(max_length=252, blank=True, null=True)
    image = models.ImageField(
        upload_to='photo',
        blank=True,
        null=True
    )


class Issue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=252, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=False)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name="created_by")
    assignee = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name="assigned_to")
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, blank=True, null=True,
                                related_name="project")
    sprint = models.ForeignKey('sprint.Sprint', on_delete=models.CASCADE, blank=True, null=True,
                               related_name="sprint")
    type = models.ForeignKey(IssueType, on_delete=models.CASCADE, blank=True, null=True,
                             related_name="sprint")
    description = models.TextField(_("Description"), blank=True, null=True)

    question_or_update = models.TextField(_("Question or Updates"), blank=True, null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    # section = models.ForeignKey('task_section_app.Section', on_delete=models.CASCADE, blank=True, null=True)
    # sections = models.ManyToManyField('task_section_app.Section', blank=True, related_name="section_tickets")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name

    @property
    def uuid(self):
        return str(self.id)

    @property
    def get_user(self):
        return self.created_by


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True,
                             related_name="comments")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, blank=True, null=True,
                              related_name="issue_comment")
    comment_text = RichTextField(_("comment"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
