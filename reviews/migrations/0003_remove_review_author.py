# Generated by Django 2.2.4 on 2019-08-21 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
    ]