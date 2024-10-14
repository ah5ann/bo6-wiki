from django.urls import path
from . import views
from .views import form_view, post, UserPostsList, PostsList, PostDetails

urlpatterns = [
    path('', post, name='postshort'),
    path('createaclass/', form_view, name='form'), 
    path('post/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('my_posts/', UserPostsList.as_view(), name='myposts'),
    path('test/', PostsList.as_view(), name='postslist'),
]