# Generated by Django 4.2.3 on 2024-03-19 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("twitter", "0005_alter_tweet_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tweet",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tweets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
