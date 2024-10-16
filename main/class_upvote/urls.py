from django.urls import path, include
from . import views
from .views import form_view, post, UserPostsList, PostsList, PostDetails
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewset)

urlpatterns = [
    path('', post, name='postshort'),
    path('createaclass/', form_view, name='form'), 
    path('post/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('my_posts/', UserPostsList.as_view(), name='myposts'),
    path('test/', PostsList.as_view(), name='postslist'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]