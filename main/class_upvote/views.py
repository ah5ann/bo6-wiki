from django.shortcuts import render, redirect
from .forms import ClassForm
from django.urls import reverse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import PostFilter

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
                created_by=request.user
            )

            # Redirect to the post details page after creation
            return redirect(reverse('postdetails'))
    else:
        form = ClassForm()

    context = {'form': form}
    return render(request, 'create_a_class.html', context)

def post(request):
    queryset = Post.objects.all() # Get all posts
    # Apply filtering
    my_filter = PostFilter(request.GET, queryset=queryset)
    filtered_queryset = my_filter.qs  # Get the filtered queryset
    
    ordered_queryset = filtered_queryset
    
    total_posts = len(ordered_queryset)
    
    sort_top = request.GET.get('sort')
    if sort_top == 'desc':
        ordered_queryset = filtered_queryset.order_by('-up_vote_total')
    elif sort_top == 'newest':
        ordered_queryset = filtered_queryset.order_by('-created_date')
    
    vote_options = ''
    
    if request.method == 'POST': 
        vote = request.POST.get('vote')
        vote_options = request.POST.get('vote_options')
    if vote_options == 'upvote':
        print(f"Up voted {vote_options} {vote}")
    elif vote_options == 'downvote':
        print(f"Down voted {vote_options} {vote}")

    # Set up pagination
    paginator = Paginator(ordered_queryset, 5)  # 5 posts per page
    page = request.GET.get('page')
    list_page = paginator.get_page(page)

    context = {
        'post_data': filtered_queryset,
        'list_page': list_page,
        'my_filter': my_filter,
        'total_posts': total_posts
    }
    return render(request, 'index.html', context)

def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'post_details.html', context)

@login_required(login_url="/accounts/login/")
def my_posts(request):
    my_posts = Post.objects.filter(created_by=request.user)
    context = {
        'my_posts': my_posts
    }
    return render(request, 'my_posts.html', context)