from django.shortcuts import render
from django.views import View
from diet_models.models import BMI


class Settings(View):
    def get(self, request):
        return render(request, 'diet_account/settings.html')


class ProfileView(View):
    def get(self, request):
        bmi = BMI.objects.all()
        return render(request, 'diet_account/profile.html', context={'bmi':bmi})



