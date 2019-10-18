# Generated by Django 2.0.13 on 2019-06-24 12:31

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('club', 'clubs'), ('sport', 'sports')], max_length=200, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('custom_venue', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(max_length=500)),
                ('link_url', models.CharField(blank=True, max_length=200, null=True)),
                ('event_date', models.DateField(auto_now_add=True)),
                ('event_time', models.TimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=200)),
                ('specification', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200, unique=True)),
                ('lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('lng', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.CreateModel(
            name='SportsandClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captain', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SportsandFacility.Category')),
                ('coach', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SportsandFacility.Facility')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='SportsandFacility.Facility'),
        ),
    ]
