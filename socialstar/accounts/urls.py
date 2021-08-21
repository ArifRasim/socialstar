from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from socialstar.accounts.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(template_name='accounts/register.html'), name='register page'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login page'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
