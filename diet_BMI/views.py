import requests
from django.shortcuts import render, redirect
from django.views import View
from diet_models.models import BMI
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from diet_BMI.forms import BMIForm
from django.urls import reverse


class CalculateBMI(View):
    template_name = 'diet_BMI/calculate.html'
    result_template = 'diet_BMI/result.html'
    api_url = "https://mega-fitness-calculator1.p.rapidapi.com/bmi"
    api_headers = {
        'X-RapidAPI-Key': 'ced2905c39msh8e7793bf9f3d485p15bc0djsn4cbc0ba6ae5a',
        "X-RapidAPI-Host": "mega-fitness-calculator1.p.rapidapi.com"
    }

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        query_params = {
            'weight': weight,
            'height': height,

        }

        response = requests.get(self.api_url, headers=self.api_headers, params=query_params)
        data = response.json()

        info = data.get('info', {})
        bmi = info.get('bmi')
        health = info.get('health')
        healthy_bmi_range = info.get('healthy_bmi_range')
        weight = query_params['weight']
        height = query_params['height']
        context = {
            'bmi': bmi,
            'healthy_bmi_range': healthy_bmi_range,
            'health': health,
            'weight': weight,
            'height': height
        }
        return render(request, self.result_template, context)


class BMICreateOrUpdateView(FormView):
    template_name = 'diet_BMI/result.html'
    success_url = reverse_lazy('index')
    form_class = BMIForm

    def get_initial(self):
        initial = super().get_initial()

        try:
            bmi_object = BMI.objects.get(user=self.request.user)
            initial['bmi'] = bmi_object.bmi
            initial['healthy_bmi_range'] = bmi_object.healthy_bmi_range
            initial['health'] = bmi_object.health
            initial['height'] = self.request.POST.get('height')
            initial['weight'] = self.request.POST.get('weight')
        except BMI.DoesNotExist:
            pass
        return initial

    def form_valid(self, form):
        defaults = {
            'bmi': form.cleaned_data['bmi'],
            'healthy_bmi_range': form.cleaned_data['healthy_bmi_range'],
            'health': form.cleaned_data['health'],
            'height': form.cleaned_data['height'],
            'weight': form.cleaned_data['weight']
        }
        bmi_object, created = BMI.objects.update_or_create(
            user=self.request.user,
            defaults=defaults
        )
        return redirect(self.success_url)