# Generated by Django 4.1.1 on 2022-10-07 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0006_alter_profile_friends"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(
                blank=True, related_name="my_friends", to="chat.friend"
            ),
        ),
    ]
