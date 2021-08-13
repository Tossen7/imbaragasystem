from django.db.models.base import Model
from django.db.models.expressions import Value
from django.db.models.fields.related import ForeignKey
import employee.models
from django.db import models
from .manager import LeaveManager
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


# Create your models here.
ANNUAL = 'annual'
CIRCUMSTANCIAL = 'circumstancial'
MATERNAL_LEAVE = 'Maternal Leave'
MARRIAGE = 'Marriage'


LEAVE_TYPE = (
(ANNUAL,'	Annual Leave'),
(CIRCUMSTANCIAL,'Circumstancial Leave'),
(MATERNAL_LEAVE, 'Maternal Leave'),
(MARRIAGE, 'Marriage Leave')
)


class Leave(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	startdate = models.DateField(verbose_name=_('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
	enddate = models.DateField(verbose_name=_('End Date'),help_text='coming back on ...',null=True,blank=False)
	leavetype = models.CharField(choices=LEAVE_TYPE,max_length=25,default=ANNUAL,null=True,blank=False)
	reason = models.CharField(verbose_name=_('Reason for Leave'),max_length=255,help_text='add additional information for leave',null=True,blank=True)
	days = models.IntegerField(verbose_name=_('Days'), help_text='Requesting Leaves', null=False, default=18)
	status = models.CharField(max_length=12,default='pending') #pending,approved,rejected,cancelled
	is_approved = models.BooleanField(default=False) #hide
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created = models.DateTimeField(auto_now=False, auto_now_add=True)


	objects = LeaveManager()


	class Meta:
		verbose_name = _('Leave')
		verbose_name_plural = _('Leaves')
		ordering = ['-created'] #recent objects



	def __str__(self):
		return ('{0} - {1}'.format(self.leavetype,self.user))




	@property
	def pretty_leave(self):
		'''
		i don't like the __str__ of leave object - this is a pretty one :-)
		'''
		leave = self.leavetype
		user = self.user
		employee = user.employee_set.first().get_full_name
		return ('{0} - {1}'.format(employee,leave))



	@property
	def leave_days(self):
		days_count = ''
		startdate = self.startdate
		enddate = self.enddate
		if startdate > enddate:
			return
		dates = (enddate - startdate)
		return dates.days




	@property
	def leave_approved(self):
		return self.is_approved == True



	@property
	def approve_leave(self):
		if not self.is_approved:
			self.is_approved = True
			self.status = 'approved'
			self.save()




	@property
	def unapprove_leave(self):
		if self.is_approved:
			self.is_approved = False
			self.status = 'pending'
			self.save()



	@property
	def leaves_cancel(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'cancelled'
			self.save()






	@property
	def reject_leave(self):
		if self.is_approved or not self.is_approved:
			self.is_approved = False
			self.status = 'rejected'
			self.save()



	@property
	def is_rejected(self):
		return self.status == 'rejected'



