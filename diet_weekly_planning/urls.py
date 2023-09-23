from django.urls import path
from diet_weekly_planning.views import Monday

urlpatterns = [
    path('monday/', Monday.as_view(), name='monday'),

]