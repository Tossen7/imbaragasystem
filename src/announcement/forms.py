from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from .models import *
from django.contrib.auth.models import User


#Anouncement
class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ['created']