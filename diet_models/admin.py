from django.contrib import admin
from diet_models.models import MealTime, Ingredient, IngredientQuantity, BMI, Weight, TimeofDay,  Meal

admin.site.register(Meal)
admin.site.register(MealTime)
admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)
admin.site.register(TimeofDay)

admin.site.register(BMI)
admin.site.register(Weight)
