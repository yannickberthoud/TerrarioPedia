# Generated by Django 4.1.7 on 2023-04-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_amphibianlifecommunity_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amphibianlifecommunity',
            options={'verbose_name': 'Amphibien : vie communautaire', 'verbose_name_plural': 'Amphibiens : vies communautaires'},
        ),
        migrations.RemoveField(
            model_name='amphibian',
            name='life_community',
        ),
        migrations.AddField(
            model_name='amphibian',
            name='life_community',
            field=models.ManyToManyField(blank=True, null=True, to='card.amphibianlifecommunity', verbose_name='Peut vivre en communauté'),
        ),
    ]
