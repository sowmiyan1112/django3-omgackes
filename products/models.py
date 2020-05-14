from django.db import models

class Homepage(models.Model):
    image_home=models.ImageField(upload_to='products/images/homeimage')


class Cakes(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    price=models.FloatField()
    image=models.ImageField(upload_to='products/images/')
    url=models.URLField(blank=True)