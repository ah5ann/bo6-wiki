from django.contrib import admin
from.models import Weapon, Attachment, AttachmentType, Category

admin.site.register(Category)
admin.site.register(Weapon)
admin.site.register(Attachment)
admin.site.register(AttachmentType)
