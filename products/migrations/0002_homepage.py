# Generated by Django 3.0.6 on 2020-05-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_home', models.ImageField(upload_to='products/images/homeimage')),
            ],
        ),
    ]
