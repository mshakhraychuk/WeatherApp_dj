from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('delete-city/<int:id>/', views.delete_city, name="delete-city"),
]
