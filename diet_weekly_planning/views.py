from diet_models.models import MealTime, Ingredient, IngredientQuantity, Meal
from diet_weekly_planning.forms import MealTimeForm, IngredientForm, MealForm, IngredientQuantityForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render, redirect
from django.views import View


class Monday(CreateView):
    success_url = reverse_lazy('monday')
    template_name = 'diet_weekly_planning/monday.html'
    model = MealTime
    form_class = MealTimeForm
    pk_url_kwarg = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brekfast'] = MealTime.objects.filter(name="Poniedzialek").filter(timeofday__name="Sniadanie")
        context['lunch'] = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Obiad")
        context['dinner'] = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Kolacja")
        context['meal'] = MealTime.objects.filter(name="Poniedzialek").filter(timeofday__name="Sniadanie")
        context['ingredientquantity'] = IngredientQuantity.objects.all()
        context['ingredients'] = Ingredient.objects.all()
        context['day'] = self.request.session.get('day_of_week', 'Poniedzialek')
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        form.save()
        return response


@receiver(user_logged_in)
def set_day(sender, request, user, **kwargs):
    import datetime

    days_of_week = ['Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela']
    today = datetime.date.today().weekday()
    day = days_of_week[today]

    request.session['day_of_week'] = day



class Ingredients(CreateView):
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


# class Recipes(CreateView):
#     def get(self, request):
#         form = MealForm()
#         return render(request, 'diet_weekly_planning/recipes.html', context={'form':form})
#
# class Monday(View):
#
#     def get(self,request):
#         brekfast = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Śniadanie")
#
#         lunch = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Obiad")
#         dinner = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Kolacja")
#         return render(request, "YourCalc/Monday.html", context={"brekfast":brekfast,"lunch":lunch,"dinner":dinner})


class AddIngredientsToMealView(View):
    def get(self, request):
        form_meal = MealForm()
        form_ingredients_quantity = IngredientQuantityForm
        return render(request, 'diet_weekly_planning/recipes.html', context={
            'form_ingredients_quantity': form_ingredients_quantity, 'form_meal': form_meal})

    def post(self, request):
        form_meal = MealForm(request.POST)
        form_ingredients_quantity = IngredientQuantityForm(request.POST)

        if form_meal.is_valid() and form_ingredients_quantity.is_valid():

            meal = form_meal.save(commit=False)
            meal.user = request.user
            meal.save()

            form_ingredients_quantity.save()

            return redirect('add_ingredients_to_meal')

        else:
            return render(request, 'diet_weekly_planning/recipes.html', context={
            'form_ingredients_quantity': form_ingredients_quantity, 'form_meal': form_meal})
