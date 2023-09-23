from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from diet_models.models import BMI
from diet_site.forms import WeightForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from diet_models.models import Weight
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'diet_site/index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bmi_data = BMI.objects.filter(user=self.request.user).first()
        if bmi_data:
            context['bmi'] = bmi_data.bmi
            context['healthy_bmi_range'] = bmi_data.healthy_bmi_range
            context['health'] = bmi_data.health
            context['height'] = bmi_data.height
            context['weight'] = bmi_data.weight
        return context


class AddWeightView(View):
    template_name = 'diet_site/index.html'
    form_class = WeightForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            weight.user = request.user
            weight.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})