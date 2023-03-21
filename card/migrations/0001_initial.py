# Generated by Django 4.1.7 on 2023-03-16 15:53

import card.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genus', models.CharField(max_length=64)),
                ('species', models.CharField(max_length=64)),
                ('is_cites', models.BooleanField()),
                ('reproduction_type', models.CharField(choices=[('O', 'Oviparous'), ('V', 'Viviparous'), ('I', 'Ovoviviparous')], max_length=1)),
                ('main_mores', models.CharField(choices=[('B', 'Borrower'), ('T', 'Terrestrial'), ('A', 'Arboreal')], max_length=1)),
                ('main_activity_perdiod', models.CharField(choices=[('N', 'Nocturnal'), ('T', 'Twilight'), ('D', 'Diurnal')], max_length=1)),
                ('is_venomous', models.BooleanField()),
                ('is_poisonous', models.BooleanField()),
                ('lower_temperature', models.IntegerField()),
                ('max_temperature', models.IntegerField()),
                ('lower_humidity', models.IntegerField()),
                ('max_humidity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Venom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('effects', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=card.models.card_directory_path)),
                ('phase', models.CharField(choices=[('J', 'Juvenil'), ('S', 'Sub adult'), ('A', 'Adult')], max_length=1)),
                ('sex', models.CharField(choices=[('U', 'Undefined'), ('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('locality', models.CharField(max_length=512)),
                ('comments', models.TextField(help_text='mutation, morphotype, hibridation')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.category'),
        ),
        migrations.AddField(
            model_name='card',
            name='venom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.venom'),
        ),
    ]
