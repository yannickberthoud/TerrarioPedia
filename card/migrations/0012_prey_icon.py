# Generated by Django 4.1.7 on 2023-03-17 17:28

import card.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0011_prey_card_comments_card_detention_difficulty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prey',
            name='icon',
            field=models.ImageField(default='', upload_to=card.models.prey_directory_path),
            preserve_default=False,
        ),
    ]
