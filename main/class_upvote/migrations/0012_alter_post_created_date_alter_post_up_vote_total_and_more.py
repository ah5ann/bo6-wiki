# Generated by Django 5.1.1 on 2024-10-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_upvote', '0011_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='post',
            name='up_vote_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.CharField(choices=[('upvote', 'UpVote'), ('downvote', 'DownVote'), ('none', 'None')], max_length=10),
        ),
    ]
