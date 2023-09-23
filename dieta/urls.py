from django.contrib import admin
from django.urls import path, include
from diet_login.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('diet_login/', include('diet_login.urls')),
    path('diet_site/', include('diet_site.urls')),
    path('diet_password_reset/', include('diet_password_reset.urls')),
    path('diet_account/', include('diet_account.urls')),
    path('diet_BMI/', include('diet_BMI.urls')),
    path('diet_change_email/', include('diet_change_email.urls')),
    path('diet_weekly_planning/', include('diet_weekly_planning.urls')),
]