# Generated by Django 5.1.1 on 2024-10-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_upvote', '0009_alter_post_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.TimeField(auto_now_add=True, verbose_name='Time created'),
        ),
    ]