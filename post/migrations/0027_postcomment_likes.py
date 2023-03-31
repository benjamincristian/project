# Generated by Django 4.1.7 on 2023-03-30 16:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0026_rename_blogcomment_postcomment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]