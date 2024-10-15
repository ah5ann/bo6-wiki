from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name  # Display category name in Django admin
    
class Attachment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attachment_name = models.CharField(max_length=30)
    attachment_type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.attachment_name} ({self.attachment_type})"


class Weapon(models.Model):
    weapon_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)

    def __str__(self):
        return self.weapon_name  # Display weapon name in Django admin


class AttachmentType(models.Model):
    attachment_type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.attachment_type_name  # Display type name in Django admin


class Post(models.Model):
    post_name = models.CharField(max_length=30)
    main_weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    attachment1 = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='post_attachment1', default=1)
    attachment2 = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='post_attachment2', default=1)
    attachment3 = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='post_attachment3', default=1)
    attachment4 = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='post_attachment4', default=1)
    attachment5 = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='post_attachment5', default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(_("Date"), auto_now_add=True)
    created_time = models.TimeField(_("Time created"), auto_now_add=True)
    up_vote_total = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.post_name} {self.id}"
    

class Vote(models.Model):
    post_voted = models.ForeignKey(Post, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.CharField(max_length=10, choices=[('upvote', 'UpVote'), ('downvote', 'DownVote'), ('none', 'None')])
    
    def __str__(self):
        return f"{self.vote} {self.post_voted.id} {self.voted_by}"