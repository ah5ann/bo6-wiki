from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassForm
from django.urls import reverse
from .models import Post, Vote, User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import PostFilter
from django.http import JsonResponse
import json
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from functions.vote import voting
from django.views.generic import DetailView

from rest_framework import permissions, viewsets
from .serializers import PostSerializer

@login_required(login_url="/accounts/login/")
def form_view(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            # Get the selected weapon and attachments from the form
            post_name = form.cleaned_data['post_name']
            main_weapon = form.cleaned_data['weapon_name']
            attachment1 = form.cleaned_data['attachment1']
            attachment2 = form.cleaned_data['attachment2']
            attachment3 = form.cleaned_data['attachment3']
            attachment4 = form.cleaned_data['attachment4']
            attachment5 = form.cleaned_data['attachment5']

            # Create a new Post object
            new_post = Post.objects.create(
                post_name=post_name,
                main_weapon=main_weapon,
                attachment1=attachment1,
                attachment2=attachment2,
                attachment3=attachment3,
                attachment4=attachment4,
                attachment5=attachment5,
                created_by=request.user,
                up_vote_total = 1 
            )
            print(f"id for new post: {new_post.id}")

            post_instance = Post.objects.get(id=new_post.id)

            vote_post = Vote.objects.create(
                post_voted=post_instance,
                voted_by=request.user,
                vote='upvote'
            )

            # Redirect to the post details page after creation
            return redirect(reverse('post_details', kwargs={'pk': new_post.id}))
    else:
        form = ClassForm()

    context = {'form': form}
    return render(request, 'create_a_class.html', context)

def post(request):
    queryset = Post.objects.all()  # Get all posts

    if queryset:
        unique = queryset[0]
        print(f"now {unique.up_vote_total}")
    
    if request.method == 'POST':
        data = json.loads(request.body)
        pk = data['vote']
        data = voting(request, pk)
        print(data)
        return JsonResponse(data)
    
    # User votes only if user is authenticated
    user_votes = []
    if request.user.is_authenticated:
        user_votes = Vote.objects.filter(voted_by=request.user).values('post_voted', 'vote')

    # Create a dictionary for quick access
    user_vote_dict = {vote['post_voted']: vote['vote'] for vote in user_votes}

    # Apply filtering
    my_filter = PostFilter(request.GET, queryset=queryset)
    filtered_queryset = my_filter.qs  # Get the filtered queryset
    
    sort_top = request.GET.get('sort')
    if sort_top == 'desc':
        filtered_queryset = filtered_queryset.order_by('-up_vote_total')
    elif sort_top == 'newest':
        filtered_queryset = filtered_queryset.order_by('-created_date')    

    # Now loop through the filtered queryset to set has_voted and user_vote
    for post in filtered_queryset:
        if post.id in user_vote_dict:
            post.has_voted = True
            post.user_vote = user_vote_dict[post.id]  # Should be 'upvote' or 'downvote'
        else:
            post.has_voted = False
            post.user_vote = None  # No vote    

    # Set up pagination
    total_posts = len(filtered_queryset)
    paginator = Paginator(filtered_queryset, 5)  # 5 posts per page
    page = request.GET.get('page')
    list_page = paginator.get_page(page)

    context = {
        'post_data': filtered_queryset,
        'list_page': list_page,
        'my_filter': my_filter,
        'total_posts': total_posts,
    }
    return render(request, 'index.html', context)

class PostDetails(DetailView):
    model = Post
    template_name = 'post_details.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Post, id=self.kwargs['pk'])
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(post=self.object)
        
        posts_voted = Vote.objects.filter(post_voted=self.object, voted_by=request.user).first()
        #posts_voted = Vote.objects.filter(post_voted=self.object, voted_by=request.user).first()
        context['posts_voted'] = posts_voted
        
        return self.render_to_response(context)
        
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if request.method == 'POST':
            data = voting(request, pk)
            print(f"this {data}")
            return JsonResponse(data)
        

@method_decorator(login_required(login_url="/accounts/login/"), name='dispatch')
class UserPostsList(ListView):
    template_name = 'my_posts.html'
    context_object_name = 'my_posts'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)


class PostsList(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('sort', '-created_date')  # Default to descending order by created_date
        return queryset.order_by(ordering)
    
class PostViewset(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]