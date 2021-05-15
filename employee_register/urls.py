
from django.urls import path
from employee_register import views

urlpatterns = [
    path('employee/', views.employee_list, name = 'employee_list'),
    path('<int:id>/', views.employee_form, name = 'employee_update'), # get and post request for the update
    path('form/', views.employee_form, name = 'employee_insert'), # get and post request for the insert 
    path('delete/<int:id>/', views.employee_delete, name = 'employee_delete')

]
