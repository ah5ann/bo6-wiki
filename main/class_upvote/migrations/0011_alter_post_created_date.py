# Generated by Django 5.0.7 on 2024-10-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_upvote', '0010_alter_post_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]