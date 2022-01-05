from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class File(models.Model):
    work_count = models.PositiveIntegerField(
        _('work count')
    )
    filename = models.CharField(
        _('file name'),
        max_length=255, 
        null=True
        )

class Work(models.Model):
    proprietary_id = models.PositiveIntegerField(
        _('proprietary id')
    )
    iswc = models.CharField(
        _('iswc'),
        max_length=255, 
        null=True
        )
    source = models.CharField(
        _('iswc'),
        max_length=255, 
        null=True
        )
    title = models.CharField(
        _('iswc'),
        max_length=255, 
        null=True
        )
    contributors = ArrayField(
        models.CharField(max_length=200), 
        blank=True
    )
