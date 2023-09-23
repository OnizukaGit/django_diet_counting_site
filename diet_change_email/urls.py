from django.urls import path
from diet_change_email.views import ChangeEmail, ChangeEmailChange, EmailChangeComplete

urlpatterns = [
    path('change-mail/', ChangeEmail.as_view(), name='change-mail'),
    path('confirm-email-change/<str:uidb64>/<str:token>/', ChangeEmailChange.as_view(), name='confirm_email_change'),
    path('email-change-complete/', EmailChangeComplete.as_view(), name='email_change_complete'),
]
