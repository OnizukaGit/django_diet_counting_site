from diet_models.models import Ingredient, IngredientQuantity, Meal
from diet_weekly_planning.forms import MealTimeForm, IngredientForm, MealForm, AddIngredientsForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class Monday(CreateView):
    template_name = 'diet_weekly_planning/monday.html'
    success_url = reverse_lazy('monday')
    form_class = MealTimeForm


class Ingredients(View):
    def get(self, request):
        form = IngredientForm()
        ingredients = Ingredient.objects.all()
        return render(request, 'diet_weekly_planning/ingredients.html', context={'form':form,
                                                                                 'ingredients':ingredients})

    def post(self, request):
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.user = request.user
            ingredient.save()
            return redirect('ingredients')
        else:
            return render(request, 'diet_weekly_planning/ingredients.html', context={'form': form})


class RecipesView(CreateView):
    template_name = "diet_weekly_planning/recipes.html"
    form_class = MealForm
    success_url = reverse_lazy('add_ingredients')
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meals = Meal.objects.all()

        context["meals"] = meals

        return context

    def form_valid(self, form):
        meal = form.save(commit=False)
        meal.user = self.request.user
        meal.save()

        self.request.session['current_meal_id'] = meal.pk
        self.success_url = reverse_lazy('add_ingredients', kwargs={'pk': meal.pk})

        return super().form_valid(form)


class AddIngredients(CreateView):
    template_name = "diet_weekly_planning/add_ingredients.html"
    form_class = AddIngredientsForm
    success_url = reverse_lazy('add_ingredients')
    pk_url_kwarg = "pk"

    def get_initial(self):
        meal_id = self.request.session.get('current_meal_id')
        return {'meal': meal_id}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meal_id = self.kwargs.get(self.pk_url_kwarg)
        meal = get_object_or_404(Meal, pk=meal_id)
        context['meals'] = meal
        context['ingredients_quantity'] = IngredientQuantity.objects.all()
        ingredients_quantity = IngredientQuantity.objects.filter(meal__pk=meal_id)

        total_ingredients_quantity = [
            {
                'ingredient': ingredient_quantity.ingredient,
                'quantity': ingredient_quantity.quantity,
                'total_gramme': ingredient_quantity.ingredient.gramme * ingredient_quantity.quantity,
                'total_calories': ingredient_quantity.ingredient.calories * ingredient_quantity.quantity,
                'total_carbohydrates': ingredient_quantity.ingredient.carbohydrates * ingredient_quantity.quantity,
                'total_protein': ingredient_quantity.ingredient.protein * ingredient_quantity.quantity,
                'total_fat': ingredient_quantity.ingredient.fat * ingredient_quantity.quantity,
            }
            for ingredient_quantity in ingredients_quantity
        ]

        total_gramme = sum(
            ingredient_quantity.ingredient.gramme * ingredient_quantity.quantity for ingredient_quantity in
            ingredients_quantity)
        total_calories = sum(
            ingredient_quantity.ingredient.calories * ingredient_quantity.quantity for ingredient_quantity in
            ingredients_quantity)
        total_carbohydrates = sum(
            ingredient_quantity.ingredient.carbohydrates * ingredient_quantity.quantity for ingredient_quantity in
            ingredients_quantity)
        total_protein = sum(
            ingredient_quantity.ingredient.protein * ingredient_quantity.quantity for ingredient_quantity in
            ingredients_quantity)
        total_fat = sum(ingredient_quantity.ingredient.fat * ingredient_quantity.quantity for ingredient_quantity in
                        ingredients_quantity)

        context['total_gramme'] = total_gramme
        context['total_calories'] = total_calories
        context['total_carbohydrates'] = total_carbohydrates
        context['total_protein'] = total_protein
        context['total_fat'] = total_fat
        context['total_ingredients_quantity'] = total_ingredients_quantity

        return context

    def form_valid(self, form):
        meal_id = self.request.session.get('current_meal_id')
        meal = get_object_or_404(Meal, pk=meal_id)

        ingredient = form.save(commit=False)
        ingredient.meal = meal
        ingredient.save()

        self.success_url = reverse_lazy('add_ingredients', kwargs={'pk': meal.pk})
        return super().form_valid(form)


class UpdateRecipes(UpdateView):
    template_name = "diet_weekly_planning/recipes.html"
    success_url = reverse_lazy('recipes')
    model = Meal
    form_class = MealForm

    def form_valid(self, form):
        meal = self.get_object()
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class DeleteRecipes(View):
    def get(self, request, pk):
        meal_id = Meal.objects.get(pk=pk)
        meal_id.delete()
        return redirect('recipes')

