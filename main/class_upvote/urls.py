from django.urls import path
from . import views
from .views import form_view, post_details

urlpatterns = [
    path('createaclass/', form_view, name='form'),   
    path('post_details/', post_details, name='postdetails')
]