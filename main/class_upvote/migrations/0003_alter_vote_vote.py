# Generated by Django 5.1.1 on 2024-10-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_upvote', '0002_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.CharField(choices=[('upvote', 'UpVote'), ('downvote', 'DownVote')], max_length=10),
        ),
    ]