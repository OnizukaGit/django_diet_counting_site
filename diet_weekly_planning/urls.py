from django.urls import path
from diet_weekly_planning.views import (Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday,
                                        Ingredients, AddIngredients,
                                        RecipesView, UpdateRecipes, DeleteRecipes, ShowTotalMeals)

urlpatterns = [
    path('monday/', Monday.as_view(), name='monday'),
    path('tuesday/', Tuesday.as_view(), name='tuesday'),
    path('wednesday/', Wednesday.as_view(), name='wednesday'),
    path('thursday/', Thursday.as_view(), name='thursday'),
    path('friday/', Friday.as_view(), name='friday'),
    path('saturday/', Saturday.as_view(), name='saturday'),
    path('sunday/', Sunday.as_view(), name='sunday'),

    path('ingredients/', Ingredients.as_view(), name='ingredients'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('add_ingredients/<int:pk>/', AddIngredients.as_view(), name="add_ingredients"),
    path('update_recipes/<int:pk>/', UpdateRecipes.as_view(), name="update_recipes"),
    path('delete_recipes/<int:pk>/', DeleteRecipes.as_view(), name="delete_recipes"),
    path('show_total_meals/<int:pk>/', ShowTotalMeals.as_view(), name="show_total_meals"),

]

