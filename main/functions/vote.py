from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from class_upvote.models import Post, Vote

def voting(request, pk):

        post = get_object_or_404(Post, id=pk)
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        vote_option = data['vote_option']
        
        if vote_option not in ['upvote', 'downvote']:
            return JsonResponse({'error': 'Invalid vote option'}, status=400)
        
        existing_vote = Vote.objects.filter(post_voted=post).first() 
        has_voted = existing_vote is not None
        
        if has_voted: 
            
            if existing_vote.vote == 'upvote' and vote_option == 'upvote':
                print(f"already clicked upvote && totalt votes = {post.up_vote_total}")
                Vote.objects.filter(id=existing_vote.id).delete()
                post.up_vote_total -= 1
                
            elif existing_vote.vote == 'downvote' and vote_option == 'downvote':
                print(f"already clicked down vote && totalt votes = {post.up_vote_total}")
                Vote.objects.filter(id=existing_vote.id).delete()
                post.up_vote_total -= 1
            
            else:        

                if existing_vote.vote == 'upvote' and vote_option == 'downvote':
                    print(f"Previous vote was upvote no its downvote && totalt votes = {post.up_vote_total}")
                    post.up_vote_total -= 1  # Decrement upvote count
                    post.save()
                    existing_vote.vote = 'downvote'  # Update the vote
                    existing_vote.save()
                elif existing_vote.vote == 'downvote' and vote_option == 'upvote':
                    print(f"Previous vote was downvote now its upvote && totalt votes = {post.up_vote_total}")
                    post.up_vote_total += 1  # Increment upvote count
                    post.save()
                    existing_vote.vote = 'upvote'  # Update the vote
                    existing_vote.save()

                    
        else:  # User is voting for the first time
            if vote_option == 'upvote':
                print(f"Vote casted as upvote && totalt votes = {post.up_vote_total}")
                post.up_vote_total += 1
                post.save()
            elif vote_option == 'downvote':
                print(f"Vote casted as downvote && totalt votes = {post.up_vote_total}")
                post.up_vote_total -= 1
                post.save()
                
            Vote.objects.create(voted_by=request.user, vote=vote_option, post_voted=post)
        
        new_vote_total = post.up_vote_total
        print(f"final total = {new_vote_total}")        
        
        # if has_voted:  # If the user has voted, we want to change their vote
        #     if existing_vote.vote == 'upvote' and vote_option == 'downvote':
        #         post.up_vote_total -= 1  # Decrement upvote count
        #         post.save()
        #         existing_vote.vote = 'downvote'  # Update the vote
        #         existing_vote.save()
        #     elif existing_vote.vote == 'downvote' and vote_option == 'upvote':
        #         post.up_vote_total += 1  # Increment upvote count
        #         post.save()
        #         existing_vote.vote = 'upvote'  # Update the vote
        #         existing_vote.save()
        # else:  # User is voting for the first time
        #     if vote_option == 'upvote':
        #         post.up_vote_total += 1
        #         post.save()
        #     elif vote_option == 'downvote':
        #         post.up_vote_total -= 1
        #         post.save()

            # Create a new Vote instance
            
        return {
            'new_vote_total' : new_vote_total,
            'new_vote' : vote_option
        }