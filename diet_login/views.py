from django.views.generic import CreateView, View, RedirectView
from django.shortcuts import render
from django.urls import reverse_lazy
from diet_login.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'diet_login/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')


class Logout(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class Register(CreateView):
    model = User
    success_url = reverse_lazy('index')
    template_name = 'diet_login/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        response = super().form_valid(form)
        cd = form.cleaned_data
        self.object.set_password(cd['password'])
        self.object.save()
        login(self.request, self.object)
        return response


class PageNotFoundView(View):
    def get(self, request):
        return render(request, 'diet_login/404.html', status=404)


custom_404_view = PageNotFoundView.as_view()


