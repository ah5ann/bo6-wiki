from django.urls import path
from . import views
from .views import form_view, post, post_details

urlpatterns = [
    path('', post, name='postshort'),
    path('createaclass/', form_view, name='form'), 
    path('post/<int:pk>', post_details, name='post_details')
]