# Generated by Django 3.2.8 on 2022-01-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read Blog Post...', max_length=255),
        ),
    ]
