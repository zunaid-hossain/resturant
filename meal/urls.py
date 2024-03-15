from django.urls import path
from .import views

urlpatterns = [
    path('',views.menu, name='menu'),
    path('item',views.home, name='meal'),
]
