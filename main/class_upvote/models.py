from django.db import models

class Weapon(models.Model):  # Model names should generally be singular
    weapon_id = models.AutoField(primary_key=True)  # Use AutoField for auto-incrementing IDs
    weapon_name = models.CharField(max_length=30)
    weapon_type = models.CharField(max_length=30)

    def __str__(self):
        return self.weapon_name  # Helps display meaningful names in Django admin

class Attachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)  # Correct use of ForeignKey
    attachment_name = models.CharField(max_length=30)
    attachment_type = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)  # Optional description

    def __str__(self):
        return f"{self.attachment_name} ({self.attachment_type})"

class AttachmentType(models.Model):
    attachment_type_id = models.AutoField(primary_key=True)
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE)  # Correct ForeignKey usage
    attachment_type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.attachment_type_name



   