from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='gov-login'),
    path('login_success', views.login_success, name='login_success'),
    path('login_failed', views.login_failed, name='login_failed')
]
