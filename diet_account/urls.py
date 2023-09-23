from django.urls import path
from diet_account.views import ProfileView, Settings

urlpatterns = [
    path('settings-view/', Settings.as_view(), name='settings'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
]
