from django import forms
from app1.models import Fee_Details_models

class Fee_details_form(forms.ModelForm):
    class Meta:
        model = Fee_Details_models
        fields = '__all__'