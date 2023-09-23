from django.urls import path
from django.contrib.auth import views as auth_view
from diet_password_reset.views import CustomPasswordChangeView, CustomPasswordResetView

urlpatterns = [
        path('reset-password/', CustomPasswordResetView.as_view
        (template_name='diet_password_reset/password_reset.html'), name='reset_password'),
        path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view
        (template_name='diet_password_reset/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>', CustomPasswordChangeView.as_view
        (template_name='diet_password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view
        (template_name='diet_password_reset/password_reset_complete.html'), name='password_reset_complete'),
    ]