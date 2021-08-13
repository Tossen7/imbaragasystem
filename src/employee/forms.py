from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from employee.models import *
from django.contrib.auth.models import User


# EMPLoYEE
class EmployeeCreateForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'onchange':'previewImage(this);'}))
	class Meta:
		model = Employee
		exclude = ['is_blocked','is_deleted','created','updated', 'employeeid']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}


class YearCreateForm(forms.ModelForm):
	class Meta:
		model = Year
		exclude = ['is_blocked','is_deleted','created','updated']
		widgets = {
				'bio':forms.Textarea(attrs={'cols':5,'rows':5})
		}


class FeedbackCreateForm(forms.ModelForm):
	class Meta:
		model = Chat
		exclude = ['created_at']


class ProjectCreateForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ['created_at']
