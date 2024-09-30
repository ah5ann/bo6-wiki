import django_filters
from .models import *

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['up_vote_total', 'created_date']