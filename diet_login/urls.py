from django.urls import path
from diet_login.views import Login, Register, Logout
from django.conf.urls import handler404
# from diet_login.views import PageNotFound


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),

]

