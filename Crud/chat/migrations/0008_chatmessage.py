# Generated by Django 4.1.1 on 2022-10-07 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0007_alter_profile_friends"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField()),
                ("seen", models.BooleanField(default=False)),
                (
                    "msg_receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="msg_receiver",
                        to="chat.profile",
                    ),
                ),
                (
                    "msg_sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="msg_sender",
                        to="chat.profile",
                    ),
                ),
            ],
        ),
    ]
