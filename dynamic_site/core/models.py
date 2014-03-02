#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class ProductType(models.Model):
    language = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

class Product(models.Model):
    language = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType)
    publish_date = models.DateTimeField()
    description = models.TextField()
