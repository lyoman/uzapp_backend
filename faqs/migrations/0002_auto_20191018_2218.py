# Generated by Django 2.2.6 on 2019-10-18 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
