from django.urls import path
from diet_weekly_planning.views import Monday, AddIngredientsToMealView, Ingredients

urlpatterns = [
    path('monday/', Monday.as_view(), name='monday'),

    path('ingredients/', Ingredients.as_view(), name='ingredients'),
    path('add_ingredients_to_meal/', AddIngredientsToMealView.as_view(), name='add_ingredients_to_meal'),

]