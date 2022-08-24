from django.urls import path

from . import views

urlpatterns = [
    path('', views.startup, name='start'),
    path('signup/', views.signup, name='signup'),
]