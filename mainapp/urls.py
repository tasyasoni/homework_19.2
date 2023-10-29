from django.urls import path
from mainapp import views


urlpatterns = [
    path('contacts/', views.contacts),
    path('', views.home)
]