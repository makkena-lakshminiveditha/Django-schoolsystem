from django import forms
from app1.models import Teacher_Details_models

class Teacher_details_form(forms.ModelForm):
    class Meta:
        model = Teacher_Details_models
        fields = '__all__'