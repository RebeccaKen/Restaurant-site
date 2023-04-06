from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from autoslug import AutoSlugField
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.urls import reverse
from datetime import datetime
from datetime import date, time



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
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, max_length=500)
    allergens = models.TextField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# model for reservations


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    number_of_guests = models.IntegerField(blank=False, default=1)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20, null=False)
    reservation_date = models.DateField(null=False, default=date(2023, 12, 31))
    reservation_time = models.TimeField(default=time(12, 0, 0))
    notes = models.CharField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"

    def get_absolute_url(self):
        return reverse('reservation_edit', args=[str(self.pk)])


# model for feedback


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()
    date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Feedback'

    def __str__(self):
        return f"{self.name}'s Feedback"

    def get_rating_display(self):
        return f"{self.rating}/5"

    get_rating_display.short_description = 'Rating'

    def save(self, *args, **kwargs):
        self.approved = False
        super().save(*args, **kwargs)


# model for customer information


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
        
    def clean(self):
        if self.user is None:
            raise ValidationError("User cannot be empty.")
