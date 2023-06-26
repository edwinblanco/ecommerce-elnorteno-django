from django.urls import path, include
from telecomunicaciones_app import views

urlpatterns = [
    path('home/', views.home_teleco, name="home-teleco"),
]