from django import forms
from diet_models.models import BMI


class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ['bmi', 'healthy_bmi_range', 'health', 'height', 'weight']