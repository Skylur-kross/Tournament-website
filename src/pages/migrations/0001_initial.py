# Generated by Django 3.2.2 on 2021-06-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_fullname', models.CharField(max_length=50)),
                ('player_login_email', models.CharField(max_length=20)),
                ('player_username', models.CharField(max_length=50)),
                ('player_Steam_id', models.IntegerField()),
                ('player_contactno', models.IntegerField()),
                ('player_Dota_rank', models.CharField(max_length=20)),
            ],
        ),
    ]