from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from diet_change_email.forms import ResetMailForm
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class ChangeEmail(View):
    template_name = 'diet_change_email/change_mail_done.html'

    def get(self, request):
        user = request.user
        first_name = user.first_name
        subject = "Temat test"
        body_template = 'diet_change_email/change_email.txt'
        uidb64 = urlsafe_base64_encode(str(user.pk).encode())
        token = default_token_generator.make_token(user)
        protocol = 'http'
        domain = 'localhost:8000'

        body = render_to_string(body_template, {'first_name':first_name, 'uidb64':uidb64, 'token':token , 'protocol':protocol, 'domain':domain})

        try:
            send_mail(subject, body, 'test@wp.pl', ['test@wp.pl'], fail_silently=False)
            return render(request, 'diet_change_email/change_mail_done.html')
        except Exception as e:
            return HttpResponse(f'JEst bład')


class EmailChangeComplete(View):
    def get(self, request):
        return render(request, 'diet_change_email/change_mail_complete.html')


class ChangeEmailChange(LoginRequiredMixin, FormView):
    model = User
    form_class = ResetMailForm
    success_url = reverse_lazy('email_change_complete')
    template_name = 'diet_change_email/change_mail_confirm.html'

    def form_valid(self, form):
        new_email = form.cleaned_data['new_email']
        user = self.request.user
        user.email = new_email

        user.save()
        return super().form_valid(form)
