from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from class_upvote.models import Post, Vote

def voting(request, pk):

    post = get_object_or_404(Post, id=pk)
    
    try:
        data = json.loads(request.body)
        print(f"data for unique post voting {data}")
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    vote_option = data['action']
    print(f"vote option {vote_option}")
    
    if vote_option not in ['upvote', 'downvote', 'none']:
        return JsonResponse({'error': 'Invalid vote option'}, status=400)
    
    Vote.objects.update_or_create(post_voted=post, voted_by=request.user, defaults={"vote": vote_option})
    post.up_vote_total = Vote.objects.filter(post_voted=post, vote="upvote").count() - Vote.objects.filter(post_voted=post, vote="downvote").count()

    post.save()
    
    new_vote_total = post.up_vote_total
        
    return {
        'new_vote_total' : new_vote_total,
        'new_vote' : vote_option,
    }