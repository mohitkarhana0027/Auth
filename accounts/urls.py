from django.urls import path
from .views import SignUpView, DashboardView
from django.contrib.auth.views import (LoginView, LogoutView)

app_name = 'account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
