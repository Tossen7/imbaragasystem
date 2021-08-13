from datetime import datetime
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from employee.utility import code_format
from django.db import models
from employee.managers import EmployeeManager
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from leave.models import Leave
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here

class Announcement(models.Model):
    message = models.TextField(max_length=500, verbose_name=_('Message'), null=False, blank=False)
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')
        ordering = ['-created']


    def __str__(self):
        return self.created