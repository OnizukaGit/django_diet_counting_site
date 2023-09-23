from diet_models.models import MealTime, Ingredient, IngredientQuantity, Meal
from diet_weekly_planning.forms import MealTimeForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


class Monday(CreateView):
    success_url = reverse_lazy('monday')
    template_name = 'diet_weekly_planning/monday.html'
    model = MealTime
    form_class = MealTimeForm
    pk_url_kwarg = 'day'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brekfast'] = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Śniadanie")
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


#
# class Monday(View):
#
#     def get(self,request):
#         brekfast = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Śniadanie")
#
#         lunch = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Obiad")
#         dinner = MealTime.objects.filter(name="Poniedziałek").filter(timeofday__name="Kolacja")
#         return render(request, "YourCalc/Monday.html", context={"brekfast":brekfast,"lunch":lunch,"dinner":dinner})
