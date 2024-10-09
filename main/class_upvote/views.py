from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClassForm
from django.urls import reverse
from .models import Post, Vote
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filters import PostFilter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

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
    queryset = Post.objects.all()  # Get all posts
    
    # User votes only if user is authenticated
    user_votes = []
    if request.user.is_authenticated:
        user_votes = Vote.objects.filter(voted_by=request.user).values('post_voted', 'vote')

    # Create a dictionary for quick access
    user_vote_dict = {vote['post_voted']: vote['vote'] for vote in user_votes}
    print("User Vote Dict:", user_vote_dict)  # Debugging output

    # Apply filtering
    my_filter = PostFilter(request.GET, queryset=queryset)
    filtered_queryset = my_filter.qs  # Get the filtered queryset

    # Now loop through the filtered queryset to set has_voted and user_vote
    for post in filtered_queryset:
        if post.id in user_vote_dict:
            post.has_voted = True
            post.user_vote = user_vote_dict[post.id]  # Should be 'upvote' or 'downvote'
        else:
            post.has_voted = False
            post.user_vote = None  # No vote
        print(f"Post ID: {post.id}, Has Voted: {post.has_voted}, User Vote: {post.user_vote}")  # Debugging output

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


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)

    # Check if the user has already voted on this post
    #existing_vote = Vote.objects.filter(post_voted=post, voted_by=request.user).first()
    existing_vote = Vote.objects.filter(post_voted=post).first() 
        
    has_voted = existing_vote is not None
    print("Has Voted?", has_voted)

    context = {
        'post': post,
        'posts_vote': existing_vote
    }
    
    return render(request, 'post_details.html', context)

def voting(request, pk):
    
    if request.method == 'POST':
        post = get_object_or_404(Post, id=pk)
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        vote_option = data['vote_option']
        post_id = data['vote']
        
        if vote_option not in ['upvote', 'downvote']:
            return JsonResponse({'error': 'Invalid vote option'}, status=400)
        
        existing_vote = Vote.objects.filter(post_voted=post).first() 
        has_voted = existing_vote is not None
        
        if has_voted:  # If the user has voted, we want to change their vote
            if existing_vote.vote == 'upvote' and vote_option == 'downvote':
                print(f"Changing vote from upvote to downvote for post id: {post_id}")
                post.up_vote_total -= 1  # Decrement upvote count
                post.save()
                existing_vote.vote = 'downvote'  # Update the vote
                existing_vote.save()
            elif existing_vote.vote == 'downvote' and vote_option == 'upvote':
                print(f"Changing vote from downvote to upvote for post id: {post_id}")
                post.up_vote_total += 1  # Increment upvote count
                post.save()
                existing_vote.vote = 'upvote'  # Update the vote
                existing_vote.save()
        else:  # User is voting for the first time
            if vote_option == 'upvote':
                print(f"{vote_option} post id: {post_id}")
                post.up_vote_total += 1
                post.save()
            elif vote_option == 'downvote':
                print(f"{vote_option} post id: {post_id}")
                post.up_vote_total -= 1
                post.save()

            # Create a new Vote instance
            Vote.objects.create(voted_by=request.user, vote=vote_option, post_voted=post)
                
        new_vote_total = post.up_vote_total
        print(f"new total {new_vote_total} ex vote {existing_vote.vote}")
        print(request.body)
            
        return JsonResponse({
            'new_vote_total' : new_vote_total,
            'new_vote' : existing_vote.vote
        })


@login_required(login_url="/accounts/login/")
def my_posts(request):
    my_posts = Post.objects.filter(created_by=request.user)
    context = {
        'my_posts': my_posts
    }
    return render(request, 'my_posts.html', context)