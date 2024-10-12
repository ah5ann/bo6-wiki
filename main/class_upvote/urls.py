from django.urls import path
from . import views
from .views import form_view, post, post_details, my_posts, PostsList

urlpatterns = [
    path('', post, name='postshort'),
    path('createaclass/', form_view, name='form'), 
    path('post/<int:pk>', post_details, name='post_details'),
    path('my_posts/', my_posts, name='myposts'),
    path('test/', PostsList.as_view(), name='postslist'),
]