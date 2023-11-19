from django.urls import path
from diet_weekly_planning.views import (Monday, Ingredients, AddIngredients, MealViewAPI, IngredientQuantityViewAPI,
                                        RecipesView,IngredientViewAPI, UpdateRecipes, DeleteRecipes)

urlpatterns = [
    path('monday/', Monday.as_view(), name='monday'),
    path('ingredients/', Ingredients.as_view(), name='ingredients'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('add_ingredients/<int:pk>/', AddIngredients.as_view(), name="add_ingredients"),
    path('update_recipes/<int:pk>/', UpdateRecipes.as_view(), name="update_recipes"),
    path('delete_recipes/<int:pk>/', DeleteRecipes.as_view(), name="delete_recipes"),

    path('ingredient-quantity-api/<int:pk>', IngredientQuantityViewAPI.as_view(), name='ingredient_quantity_api'),
    path('meal-api/<int:pk>', MealViewAPI.as_view(), name='meal_api'),
    path('ingredient-api/<int:pk>', IngredientViewAPI.as_view(), name='ingredient-api'),

]

