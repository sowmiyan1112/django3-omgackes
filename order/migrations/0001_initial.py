# Generated by Django 3.0.6 on 2020-05-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputEmail', models.EmailField(max_length=50)),
                ('inputPhonenumber', models.FloatField()),
                ('inputcaketype', models.CharField(max_length=50)),
                ('inputQuantity', models.FloatField()),
                ('inputComments', models.CharField(max_length=500)),
                ('inputAddress', models.CharField(max_length=500)),
                ('inputCity', models.CharField(max_length=50)),
                ('inputState', models.CharField(max_length=50)),
                ('inputZip', models.FloatField(max_length=7)),
            ],
        ),
    ]
