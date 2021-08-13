from employee.views import dashboard
from django.urls import path
from .import views


app_name = 'dashboard'

urlpatterns = [
    path('welcome/',views.dashboard,name='dashboard'),

    # Employee
    path('employees/all/',views.dashboard_employees,name='employees'),
    path('employee/create/',views.dashboard_employees_create,name='employeecreate'),
    path('employee/profile/<int:id>/',views.dashboard_employee_info,name='employeeinfo'),
    path('employee/profile/edit/<int:id>/',views.employee_edit_data,name='edit'),
    path('employees/create/days/', views.dashboard_days_create, name='createdays'),
    path('employees/view/days/', views.dashboard_view_days, name='viewdays'),
    path('employees/leave/rejected/feedback/', views.feedback_view, name='feedback'),
    path('employees/leave/feedback/create/', views.dashboard_feedback_create, name='createfeedback'),
    path('employees/leave/project/create_view', views.dashboard_project_create, name='createproject'),
    path('employees/leave/rejected/feedback', views.feedback_for_epmloyee, name='employeefeedback'),
    path('employees/announcement/create', views.dashboard_announcement_create, name = 'announcementcreate'),
    path('employees/announcement/view', views.announcement_view, name = 'announcementview'),


    # # Emergency
    # path('emergency/create/',views.dashboard_emergency_create,name='emergencycreate'),
    # path('emergency/update/<int:id>',views.dashboard_emergency_update,name='emergencyupdate'),

    # # Family
    # path('family/create/',views.dashboard_family_create,name='familycreate'),
    # path('family/edit/<int:id>',views.dashboard_family_edit,name='familyedit'),
    
    # #Bank
    # path('bank/create/',views.dashboard_bank_create,name='bankaccountcreate'),

    #---work-on-edit-view------#
    # path('bank/edit/<int:id>/',views.employee_bank_account_update,name='accountedit'),
    path('leave/apply/',views.leave_creation,name='createleave'),
    path('leaves/pending/all/',views.leaves_list,name='leaveslist'),
    path('leaves/approved/all/',views.leaves_approved_list,name='approvedleaveslist'),
    path('leaves/cancel/all/',views.cancel_leaves_list,name='canceleaveslist'),
    path('leaves/all/view/<int:id>/',views.leaves_view,name='userleaveview'),
    path('leaves/view/table/',views.view_my_leave_table,name='staffleavetable'),
    path('leave/approve/<int:id>/',views.approve_leave,name='userleaveapprove'),
    path('leave/unapprove/<int:id>/',views.unapprove_leave,name='userleaveunapprove'),
    path('leave/cancel/<int:id>/',views.cancel_leave,name='userleavecancel'),
    path('leave/uncancel/<int:id>/',views.uncancel_leave,name='userleaveuncancel'),
    path('leaves/rejected/all/',views.leave_rejected_list,name='leavesrejected'),
    path('leave/reject/<int:id>/',views.reject_leave,name='reject'),
    path('leave/unreject/<int:id>/',views.unreject_leave,name='unreject')
    # BIRTHDAY ROUTE
    # path('birthdays/all/',views.birthday_this_month,name='birthdays'),



]
