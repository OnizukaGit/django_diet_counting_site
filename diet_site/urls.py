from django.urls import path
from diet_site.views import IndexView, AddWeightView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('add_weight/', AddWeightView.as_view(), name='add_weight'),

]