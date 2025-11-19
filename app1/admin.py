from django.contrib import admin

# Register your models here.
from app1.models import Teacher_Details_models,Student_Details_models,Fee_Details_models

class Teacher_Admin(admin.ModelAdmin):
    list_display = ['teacher_id','Name','Age','Subject','Email','Phone','Salary']

admin.site.register(Teacher_Details_models,Teacher_Admin)

class Student_Admin(admin.ModelAdmin):
    list_display = ['Student_id','StudentName','FatherName','Age','Grade','Email','Phone']

admin.site.register(Student_Details_models,Student_Admin)


class Fee_Admin(admin.ModelAdmin):
    list_display = ['Fee_id','StudentName','Total_fee','Amount_paid','Pnding_fee','Payment_date']

admin.site.register(Fee_Details_models,Fee_Admin)