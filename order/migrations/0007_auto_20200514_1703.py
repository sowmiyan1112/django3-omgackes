# Generated by Django 3.0.6 on 2020-05-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200514_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Phonenumber',
            field=models.CharField(max_length=10),
        ),
    ]
