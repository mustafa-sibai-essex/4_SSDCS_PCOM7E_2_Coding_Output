from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login_user', views.login_user, name='login_user'),
    path('login_success', views.login_success, name='login_success'),
    path('login_failed', views.login_failed, name='login_failed')
]