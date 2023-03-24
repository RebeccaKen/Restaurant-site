from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# model for Menu

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_detail', args=[str(self.id)])

# model for MenuItems

class MenuItem(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True, max_length=500)
    allergens = models.TextField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_detail', args=[str(self.menu.id)])

    



