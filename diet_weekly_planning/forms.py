from django import forms
from diet_models.models import MealTime, Ingredient, Meal, IngredientQuantity


class MealTimeForm(forms.ModelForm):
    class Meta:
        model = MealTime
        fields = ['timeofday', 'meal']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['user']


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['description']


class IngredientQuantityForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ['ingredient', 'quantity', 'meal']