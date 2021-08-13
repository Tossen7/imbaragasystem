from datetime import datetime
from django.db.models.deletion import CASCADE
from employee.utility import code_format
from django.db import models
from employee.managers import EmployeeManager
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from leave.models import Leave
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Project(models.Model):

    name = models.CharField(max_length=125, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['name','created_at']


    def __str__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name','created']


    def __str__(self):
        return self.name


class Department(models.Model):


    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name','created']
    
    def __str__(self):
        return self.name


class Employee(models.Model):

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    NOT_KNOWN = 'Not Known'

    GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    (OTHER,'Other'),
    (NOT_KNOWN,'Not Known'),
    )

    MR = 'Mr'
    MRS = 'Mrs'
    MSS = 'Mss'
    DR = 'Dr'
    SIR = 'Sir'
    MADAM = 'Madam'

    TITLE = (
    (MR,'Mr'),
    (MRS,'Mrs'),
    (MSS,'Mss'),
    (DR,'Dr'),
    (SIR,'Sir'),
    (MADAM,'Madam'),
    )


    FIXED_TERM_CONTRACT = 'Fixed Term Contract'
    Open_Ended_Contract = 'Open Ended Contract'
    INTERN = 'Intern'
    VOLUNTEER = 'Volunteer'

    EMPLOYEETYPE = (
    (FIXED_TERM_CONTRACT,'Fixed Term Contract'),
    (Open_Ended_Contract,'Open Ended Contact'),
    (INTERN,'Intern'),
    (VOLUNTEER, 'Volunteer'),
    )


    
    
    # PERSONAL DATA
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    image = models.FileField(_('Profile Image'),upload_to='profiles',default='default.png',blank=True,null=True,help_text='upload image size less than 2.0MB')#work on path username-date/image
    firstname = models.CharField(_('Firstname'),max_length=125,null=False,blank=False)
    lastname = models.CharField(_('Lastname'),max_length=125,null=False,blank=False)
    othername = models.CharField(_('Othername (optional)'),max_length=125,null=True,blank=True)
    birthday = models.DateField(_('Birthday'),blank=False,null=False)
    department =  models.ForeignKey(Department,verbose_name =_('Location'),on_delete=models.SET_NULL,null=True,default=None)
    project = models.ForeignKey(Project, verbose_name = 'Project', on_delete = models.CASCADE, null = True, blank = True)
    role =  models.ForeignKey(Role,verbose_name =_('Position'),on_delete=models.SET_NULL,null=True,default=None)
    startdate = models.DateField(_('Employment Start Date'),help_text='date of employment',blank=False,null=True)
    employeetype = models.CharField(_('Employee Type'),max_length=200,default=FIXED_TERM_CONTRACT,choices=EMPLOYEETYPE,blank=False,null=True)
    employeeid = models.CharField(_('Employee ID Number'),max_length=10,null=True,blank=True, default='AB125')
    gender = models.CharField(_('Gender'),max_length=15,default=NOT_KNOWN,choices=GENDER,blank=False,null=True)
    present_year = models.PositiveIntegerField(_('Days in this Year'), blank=True, null=True, default=18)
    last_year = models.PositiveIntegerField(_('Days in last Year'), blank = True, null = True, default = 18)
    
    # app related
    is_blocked = models.BooleanField(_('Is Blocked'),help_text='button to toggle employee block and unblock',default=False)
    is_deleted = models.BooleanField(_('Is Deleted'),help_text='button to toggle employee deleted and undelete',default=False)
    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)


    #PLUG MANAGERS
    objects = EmployeeManager()

    
    
    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']


    def __str__(self):
        return self.get_full_name


    @property
    def get_full_name(self):
        fullname = ''
        firstname = self.firstname
        lastname = self.lastname
        othername = self.othername

        if (firstname and lastname) or othername is None:
            fullname = firstname +' '+ lastname
            return fullname
        elif othername:
            fullname = firstname + ' '+ lastname +' '+othername
            return fullname
        return


    @property
    def get_total_day(self):
        totalday = ''
        last_year = self.last_year
        present_year = self.present_year
        totalday = last_year + present_year

        return totalday

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return



    @property
    def can_apply_leave(self):
        pass

   


    def save(self,*args,**kwargs):
        '''
        overriding the save method - for every instance that calls the save method 
        perform this action on its employee_id

        '''
        get_id = self.employeeid #grab employee_id number from submitted form field
        data = code_format(get_id)
        self.employeeid = data #pass the new code to the employee_id as its orifinal or actual code
        super().save(*args,**kwargs) # call the parent save method
        # print(self.employeeid)


class Year(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'),on_delete=CASCADE)
    present_year = models.PositiveIntegerField(_('Days in this Year'), blank=False, null=True, default=18)
    last_year = models.PositiveIntegerField(_('Days in last Year'), blank = False, null = False, default = 18)
    

@property
def get_total_days(self):
         totaldays = ''
         present_year = self.present_year
         last_year = self.last_year

         totaldays = present_year + last_year 
         return totaldays

class Meta:
        verbose_name = _('Year')
        verbose_name_plural = _('Years')
        ordering = ['-employee']
    
def __str__(self):
   return self.employee


class Feedback(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=_('Employee'), on_delete=CASCADE)
    leave = models.ForeignKey(Leave, verbose_name='Leave', on_delete=CASCADE)
    feeback = models.TextField(_('Message'), max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = _('Feedback')
    verbose_name_plural = _('Feedbacks')
    ordering = ['-id']

def __str__(self):
    return self.employee


class Chat(models.Model):
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=CASCADE)
    leave = models.ForeignKey(Leave, verbose_name='Leave', on_delete=CASCADE)
    feeback = models.TextField(_('Message'), max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = _('Feedback')
    verbose_name_plural = _('Feedbacks')
    ordering = ['-id']

def __str__(self):
    return self.employee

