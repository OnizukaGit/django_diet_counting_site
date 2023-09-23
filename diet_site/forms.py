from django import forms
from diet_models.models import Weight


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = {'weight'}