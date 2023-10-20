from django.contrib import admin

# Register your models here.

from .models import Categorie, Product

admin.site.register(Categorie)
admin.site.register(Product)
