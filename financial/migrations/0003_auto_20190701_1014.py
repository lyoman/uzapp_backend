# Generated by Django 2.0.13 on 2019-07-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0002_auto_20190701_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialstatement',
            name='credit',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='financialstatement',
            name='debit',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
