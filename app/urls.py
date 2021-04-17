

from django.urls import include, path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('create/',views.create_employee,name='create_employee'),

    path(r'^api/employees/$', views.employee_list,name='employees'),
    path(r'^api/employees/(?P<pk>[0-9]+)$', views.employee_detail),
    # path('api/employees/',views.employees,name='employees')
    ]