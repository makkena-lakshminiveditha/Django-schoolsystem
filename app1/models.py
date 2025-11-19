from django.db import models

# Create your models here.
class Teacher_Details_models(models.Model):
    teacher_id = models.IntegerField(unique=True)
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone = models.BigIntegerField(unique=True)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.Name

class Student_Details_models(models.Model):
    Student_id = models.IntegerField(unique=True)
    StudentName = models.CharField(max_length=100)
    FatherName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Grade = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    Phone = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.StudentName
    
class Fee_Details_models(models.Model):
    Fee_id = models.IntegerField(unique=True)
    StudentName = models.CharField(max_length=100)
    Total_fee = models.DecimalField(max_digits=10,decimal_places=2)
    Amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    Pnding_fee = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_date = models.DateField()

    def __str__(self):
        return str(self.Fee_id)
