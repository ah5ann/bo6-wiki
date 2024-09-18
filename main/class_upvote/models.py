from django.db import models

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
