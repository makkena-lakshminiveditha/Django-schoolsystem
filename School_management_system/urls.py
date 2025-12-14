"""
URL configuration for School_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import home_page,Student_Details,Student_form,Student_update_data,Student_delete_data
from app1.views import Employes_Details,Employe_form,Employe_update_data,Employe_delete_data
from app1.views import fee_Details,Fee_form,Fee_update_data,Fee_delete_data
from app1.views import registration_form,login_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',registration_form,name ='regi101'),
    path('login1',login_form,name = 'login101'),
    path('home101',home_page,name='myhomepage'),
    path('students/',Student_Details,name='mystudents'),
    path('studentform/',Student_form,name = 'mystudentform'),
    path('update/<int:id>/',Student_update_data,name='studentupdate'),
    path('delete/<int:id>/',Student_delete_data,name='studentdelete'),

    path('employes/',Employes_Details,name='myemployes'),
    path('employeform/',Employe_form,name = 'myemployeform'),
    path('update1/<int:id>/',Employe_update_data,name='employeupdate'),
    path('delete1/<int:id>/',Employe_delete_data,name='employedelete'),

    path('fee/',fee_Details,name='myfee'),
    path('feeform/',Fee_form,name='myfeeform'),
    path('update2/<int:id>/',Fee_update_data,name='feeupdate'),
    path('delete2/<int:id>/',Fee_delete_data,name='feedelete')


]
