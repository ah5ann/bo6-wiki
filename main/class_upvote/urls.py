from django.urls import path
from . import views
from .views import form_view

urlpatterns = [
    path('', form_view, name='form'),   
]