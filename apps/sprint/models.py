import uuid

from django.db import models
from django.utils.translation import gettext as _
# Create your models here


class Sprint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=556, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    completed_date = models.DateField()
    goal = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Sprint')
        verbose_name_plural = _('Sprints')
        app_label = 'sprint'

    def __str__(self):
        if not self.name:
            return " title IS NULL"
        return self.name
