# Generated by Django 2.1.3 on 2018-11-24 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Plural', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='second_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_second_player', to=settings.AUTH_USER_MODEL),
        ),
    ]
