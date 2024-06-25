from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=60)
    category = models.CharField(max_length=60)
    price = models.IntegerField()
    image = models.FileField(max_length=200, upload_to="products/",null=True)