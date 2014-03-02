#-*- coding:utf-8 -*-
import datetime
from django.db import models

# Create your models here.


class ProductType(models.Model):
    language = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.name


class Product(models.Model):
    language = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    pic = models.ImageField(upload_to="uploads/products")
    product_type = models.ForeignKey(ProductType)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField()

    def __unicode__(self):
        return self.name


class AboutUs(models.Model):
    pic = models.ImageField(upload_to="uploads")
    content = models.TextField(max_length=10000)