# coding: utf-8

from django.contrib import admin
from dynamic_site.core.models import ProductType, Product, AboutUs


class ProductTypeAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class AboutUsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(AboutUs, AboutUsAdmin)