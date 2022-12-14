# Generated by Django 4.1.1 on 2022-10-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0003_remove_profile_friends"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="my_friends", to="chat.friend"
            ),
        ),
    ]
