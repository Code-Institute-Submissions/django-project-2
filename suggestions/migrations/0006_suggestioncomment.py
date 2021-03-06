# Generated by Django 2.2.4 on 2019-09-06 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestions', '0005_auto_20190902_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='suggestions.Suggestion')),
            ],
        ),
    ]
