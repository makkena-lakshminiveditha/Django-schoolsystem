from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Student_Details_models,Teacher_Details_models,Fee_Details_models
from app1.formstudent1 import Student_details_form
from app1.formstudentupdate import Student_update_form
from app1.formemploye1 import Teacher_details_form
from app1.formemployeupdate import Teacher_update_form
from app1.formfee1 import Fee_details_form
from app1.formfeeupdate import Fee_update_form

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
def registration_form(request):
    message = ''
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_email = request.POST.get('useremail')
        user_password = request.POST.get('userpassword')
        user_repassword = request.POST.get('reuserpassword')

        if user_password != user_repassword:
            message = 'Passwords do not match'
        elif User.objects.filter(email=user_email).exists():
            message = 'User already exists'
        else:
            user = User.objects.create_user(
                username=user_name,
                email=user_email,
                password=user_password
            )
            user.save()
            return redirect('login101')

    return render(request, 'frontend_app1/register.html', {'message': message})
def login_form(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('login_name')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            message = 'login Succesfully'
            return redirect('myhomepage')   
        else:
            message = 'Invalid username or password'

    return render(request, 'frontend_app1/login1.html', {'message': message})

#-------------------------------------------HOME---------------------------------------------------
def home_page(request):
    return render(request,'frontend_app1/home.html')

def Employes_Details(request):
    Teacher = Teacher_Details_models.objects.all()
    contest = {
        'Teacher':Teacher
    }
    return render(request,'frontend_app1/employetable.html',contest)

def Employe_form(request):
    if request.method == 'POST':
        form = Teacher_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myemployes')
        else:
            return HttpResponse('Invaild Data')
    else:
        form = Teacher_details_form()
    contest = {
        'form':form
    }
    return render(request,'frontend_app1/employeform.html',contest)
def Employe_update_data(request,id):
    data = Teacher_Details_models.objects.get(id=id)
    if request.method == 'POST':
        form = Teacher_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('myemployes')
    else:
        form = Teacher_update_form(instance=data)
    contest = {
        'form':form
    }
    return render(request,'frontend_app1/employeupdate.html',contest)

def Employe_delete_data(request,id):
    data = Teacher_Details_models.objects.get(id=id)
    data.delete()
    return redirect('myemployes')

#-------------------------------------------Student Data-------------------------------------------

def Student_Details(request):
    student = Student_Details_models.objects.all()
    contest = {
        'student': student
    }
    return render(request,'frontend_app1/studenttable.html',contest)
def Student_form(request):
    if request.method == 'POST':
        form = Student_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mystudents')
        else:
            return HttpResponse('Invaild Data')
    else:
        form = Student_details_form()
        contest = {
            'form':form
        }
        return render(request,'frontend_app1/studentform.html',contest)
    
def Student_update_data(request,id):
    data = Student_Details_models.objects.get(id=id)
    if request.method == 'POST':
        form = Student_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('mystudents')
    else:
        form = Student_update_form(instance=data)
    contest = {
        'form':form
    }
    return render(request,'frontend_app1/studentupdate.html',contest)

def Student_delete_data(request,id):
    data = Student_Details_models.objects.get(id=id)
    data.delete()
    return redirect('mystudents')
#----------------------------------------------------Fee Data-------------------------------------------------------

def fee_Details(request):
    fee = Fee_Details_models.objects.all()
    contest = {
        'fee':fee
    }
    return render(request,'frontend_app1/feetable.html',contest)
def Fee_form(request):
    if request.method == 'POST':
        form = Fee_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myfee')
        else:
            return HttpResponse('Invaild Data')
    else:
        form = Fee_details_form()
        contest = {
            'form':form
        }
        return render(request,'frontend_app1/feeform.html',contest)
    
def Fee_update_data(request,id):
    data =Fee_Details_models.objects.get(id=id)
    if request.method == 'POST':
        form = Fee_update_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('myfee')
    else:
        form = Fee_update_form(instance=data)
    contest = {
        'form':form
    }
    return render(request,'frontend_app1/feeupdate.html',contest)

def Fee_delete_data(request,id):
    data = Fee_Details_models.objects.get(id=id)
    data.delete()
    return redirect('myfee')

