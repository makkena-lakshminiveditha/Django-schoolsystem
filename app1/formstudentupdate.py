from django import forms
from app1.models import Student_Details_models

class Student_update_form(forms.ModelForm):
    class Meta:
        model = Student_Details_models
        fields = '__all__'