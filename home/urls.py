from django.urls import path, include
from . import views

urlpatterns = [
    path('set1', include('set1.urls')),
    path('', views.index, name='index'),
]
