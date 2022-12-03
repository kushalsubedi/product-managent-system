from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    stock = models.IntegerField(null=True)
    description=models.TextField(null=True)
    #image_url = models.CharField(max_length=2083)
    time= models.TimeField(auto_now=True)

    def __str__(self):
        return self.name

