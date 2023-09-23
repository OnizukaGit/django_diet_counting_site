from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import MealTime


@receiver(user_signed_up)
def create_weekly_meal_plan(sender, request, user, **kwargs):
    days_of_week = [option[0] for option in MealTime.options]

    for day in days_of_week:
        MealTime.objects.create(name=day, user=user)
