from diet_models.models import IngredientQuantity, Meal, Ingredient
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class IngredientQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientQuantity
        fields = ('ingredient', 'quantity')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'description')

