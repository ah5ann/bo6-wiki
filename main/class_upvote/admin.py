from django.contrib import admin
from.models import Weapon, Attachment, AttachmentType, Category, Post, Vote

admin.site.register(Category)
admin.site.register(Weapon)
admin.site.register(Attachment)
admin.site.register(AttachmentType)
admin.site.register(Post)
admin.site.register(Vote)