# Generated by Django 2.0.13 on 2019-07-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodordering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodorder',
            name='status',
            field=models.CharField(default='pending', max_length=200),
        ),
    ]
