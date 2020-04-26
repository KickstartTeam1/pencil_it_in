from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-event/', views.create_event, name='create_event'),
    path('edit-event/<event_id>/', views.edit_event, name='edit_event'),
    path('event/<event_id>/', views.event, name='event'),
]
