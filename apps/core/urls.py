from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-event/', views.create_event, name='create-event'),
]
