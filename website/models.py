from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name



class Product(models.Model):
    catagory = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False,)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=False)
    size = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name