from django.contrib import admin
from employee.models import *



admin.site.register(Role)
admin.site.register(Department)

admin.site.register(Employee)
admin.site.register(Year)
admin.site.register(Feedback)
admin.site.register(Project)
admin.site.register(Chat)