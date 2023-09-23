from django import forms
from diet_models.models import MealTime


class MealTimeForm(forms.ModelForm):
    class Meta:
        model = MealTime
        fields = ['timeofday', 'meal']