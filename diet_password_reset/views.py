from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from diet_password_reset.forms import CustomPasswordChangeForm
from django.urls import reverse_lazy


class CustomPasswordChangeView(PasswordResetConfirmView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'diet_password_reset/password_reset.html'
    email_template_name = 'registration/password_reset_email_custom.txt'
    success_url = reverse_lazy('password_reset_done')
