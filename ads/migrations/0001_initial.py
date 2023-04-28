# Generated by Django 4.1.7 on 2023-04-24 18:07

import ads.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A', 'Amphibiens'), ('L', 'Lézards'), ('S', 'Serpents'), ('M', 'Matériels et terrarium')], max_length=1, verbose_name='Catégorie')),
                ('type_of_ads', models.CharField(choices=[('R', 'Recherche'), ('V', 'Vends')], max_length=1, verbose_name="Type d'annonce")),
                ('image', models.ImageField(blank=True, upload_to=ads.models.ads_directory_path)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
