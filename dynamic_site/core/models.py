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
    pic = models.ImageField(upload_to="uploads/products")
    product_type = models.ForeignKey(ProductType)
    publish_date = models.DateTimeField()
    description = models.TextField()


class AboutUs(models.Model):
    pic = models.ImageField(upload_to="uploads")
    content = models.TextField(max_length=10000)