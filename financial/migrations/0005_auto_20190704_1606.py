# Generated by Django 2.0.13 on 2019-07-04 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_auto_20190704_1445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financialstatement',
            options={'ordering': ['timestamp', '-updated']},
        ),
    ]
