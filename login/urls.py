from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_index, name='login_index'),
    path('register', views.register, name='register'),
    path('logout', views.user_logout, name='user_logout'),
]