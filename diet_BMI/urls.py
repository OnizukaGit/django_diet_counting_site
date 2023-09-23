from django.urls import path
from diet_BMI.views import CalculateBMI, BMICreateOrUpdateView

urlpatterns = [
    path('calculate/', CalculateBMI.as_view(), name='calculate_and_result'),
    path('create/', BMICreateOrUpdateView.as_view(), name='create_bmi'),
]