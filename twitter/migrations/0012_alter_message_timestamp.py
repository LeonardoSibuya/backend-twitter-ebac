# Generated by Django 4.2.3 on 2024-04-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("twitter", "0011_conversation_message_delete_chatmessage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
