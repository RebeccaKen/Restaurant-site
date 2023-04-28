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


class Menu(models.Model):
    """
    A model representing a menu item.

    Attributes:
        name (str): The name of the menu item.
        description (str, optional): A brief description of the menu item (default '').

    Methods:
        __str__(): Returns a string representation of the menu item.
        get_absolute_url(): Returns the URL for accessing the detail view of the menu item.
    """

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
        """
        Returns a string representation of the menu item.

        Returns:
            str: The name of the menu item.
        """

    def get_absolute_url(self):
        """
        Returns the URL for accessing the detail view of the menu item.

        Returns:
            str: The URL for the detail view of the menu item.
        """
    return reverse('menu_detail', args=[str(self.id)])

class MenuItem(models.Model):
    """
    A model representing a single item on a menu.

    Attributes:
        name (str): The name of the menu item.
        slug (str): A unique slugified version of the menu item name.
        description (str, optional): A brief description of the menu item (default '').
        allergens (str, optional): A list of allergens contained in the menu item (default '').
        price (decimal): The price of the menu item.
        menu (Menu): The menu that this item belongs to.
        updated_on (datetime): The date and time when the menu item was last updated.
        created_on (datetime): The date and time when the menu item was created.

    Methods:
        __str__(): Returns a string representation of the menu item.
    """

    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True, max_length=500)
    allergens = models.TextField(blank=True, max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    menu = models.ForeignKey(Menu, related_name='menu', on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the menu item.

        Returns:
            str: The name of the menu item.
        """
    return self.name


# model for reservations


class Reservation(models.Model):
    """
    The Reservation model represents a reservation made by a user. 
    It includes the user's information (if available), the reservation 
    details such as name, number of guests, email, phone, date and time 
    of reservation, notes, slug, creation date, and approval status.

    Attributes:
        user: ForeignKey to the User model. Represents the user who made the reservation.
        name: CharField. The name for the reservation.
        number_of_guests: IntegerField. The number of guests for the reservation.
        email: EmailField. The email address for the reservation.
        phone: CharField. The phone number for the reservation.
        reservation_date: DateField. The date of the reservation.
        reservation_time: TimeField. The time of the reservation.
        notes: CharField. Additional notes for the reservation.
        slug: AutoSlugField. A slug to represent the reservation, generated from the name field.
        created_at: DateTimeField. The date and time when the reservation was created.
        is_approved: BooleanField. Indicates whether the reservation has been approved.
    
    Methods:

        str(self): Returns a string representation of the reservation.
        get_absolute_url(self): Returns the URL for editing the reservation.
    """

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
          """
        Returns a string representation of the reservation.

        Returns:
            str: A string in the format "Reservation for {name} on {reservation_date} at {reservation_time}".
        """
    return f"Reservation for {self.name} on {self.reservation_date} at {self.reservation_time}"

    def get_absolute_url(self):
        """
        Returns the URL for accessing the edit view of the reservation.

        Returns:
            str: The URL for the edit view of the reservation.
        """
    return reverse('reservation_edit', args=[str(self.pk)])


# model for feedback


class Feedback(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
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
