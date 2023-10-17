from diet_models.models import MealTime, Ingredient, IngredientQuantity, Meal
from diet_weekly_planning.forms import MealTimeForm, IngredientForm
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


from django.http import Http404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from diet_weekly_planning.serializers import IngredientQuantitySerializer, MealSerializer, IngredientSerializer


class IngredientQuantityViewAPI(generics.ListCreateAPIView):
    queryset = IngredientQuantity.objects.all()
    serializer_class = IngredientQuantitySerializer


class MealViewAPI(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class IngredientViewAPI(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipesView(View):
    def get(self, request):
        return render(request, 'diet_weekly_planning/recipes.html')
















