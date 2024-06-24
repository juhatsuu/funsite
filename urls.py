from django.urls import path
from . import views
from .views import process_function

urlpatterns = [
    path('process', process_function),
    path('', views.index)
]
