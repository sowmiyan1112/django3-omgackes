from django.db import models




class Order(models.Model):
    Email=models.EmailField()
    Phonenumber=models.CharField(max_length=10)
    caketype=models.CharField(max_length=500)
    Quantity=models.FloatField(default='1.5')
    Comments=models.CharField(max_length=500)
    Address=models.CharField(max_length=500)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)








