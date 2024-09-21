from django.urls import path
from . import views
from .views import form_view

urlpatterns = [
    path('createaclass/', form_view, name='form'),   
    #path('createaclass/', create_a_class_view, name='createaclass')
]