from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    gramme = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    calories = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbohydrates = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IngredientQuantity(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Posiłek: {self.meal}, {self.ingredient}, Ilość : {self.quantity}"


class TimeofDay(models.Model):
    options = (
        ('Sniadanie','Śniadanie'),
        ('Obiad', 'Obiad'),
        ('Kolacja', 'Kolacja'),
    )

    name = models.CharField(choices=options)

    def __str__(self):
        return self.name


class MealTime(models.Model):
    DAY_CHOICES = (
        ('Mon', 'Poniedziałek'),
        ('Tue', 'Wtorek'),
        ('Wed', 'Środa'),
        ('Thu', 'Czwartek'),
        ('Fri', 'Piątek'),
        ('Sat', 'Sobota'),
        ('Sun', 'Niedziela'),
    )

    day = models.CharField(choices=DAY_CHOICES, max_length=3, default='Mon')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True, blank=True)
    timeofday = models.ForeignKey(TimeofDay, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.meal}"


class BMI(models.Model):
    bmi = models.CharField(max_length=10)
    healthy_bmi_range = models.CharField(max_length=100)
    health = models.CharField(max_length=100)
    weight = models.CharField(max_length=64, default='0')
    height = models.CharField(max_length=64, default='0')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"BMI: {self.bmi}, User: {self.user.first_name}"


class Weight(models.Model):
    weight = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Waga: {self.weight}, User: {self.first_name}"



