# Generated by Django 4.1.7 on 2023-03-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0014_environment_card_environments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardimage',
            name='comments',
            field=models.TextField(blank=True, help_text='mutation, morphotype, hybridation'),
        ),
    ]
