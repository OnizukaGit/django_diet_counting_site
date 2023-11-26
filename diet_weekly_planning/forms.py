from django import forms
from diet_models.models import MealTime, Ingredient, Meal, IngredientQuantity


class MealTimeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        current_day = kwargs.pop('current_day', None)
        super().__init__(*args, **kwargs)
        if current_day:
            self.fields['day'].initial = current_day
    class Meta:
        model = MealTime
        fields = ['day','timeofday', 'meal']
        widgets = {
            'day' : forms.HiddenInput(),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['user']


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description']


class AddIngredientsForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ['ingredient', 'quantity']
