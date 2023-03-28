from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone



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
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_detail', args=[str(self.menu.id)])


# model for reservations


class Reservation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    notes = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return f"Reservation for {self.party_size} people on {self.date} at {self.time}"


# model for orders


class Order(models.Model):
    name = models.CharField(max_length=100, null=False, default='Default Name')
    order_date = models.DateTimeField(auto_now=True)
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return f"Order #{self.id} for {self.customer.name}"

    class Meta:
        ordering = ['-order_date']

    def total_cost(self):
        return sum(item.price for item in self.items.all())


# model for customer information


class Customer(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(default='', editable=False, max_length=100)

    def __str__(self):
        return self.name


# class for contact information 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.submitted_at}"


