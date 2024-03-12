from django.urls import path
from reminders import views

urlpatterns = [
    path('', views.index, name='index'),  # Default view for root URL
    path('api/create-reminder/', views.create_reminder, name='create_reminder'),
]
