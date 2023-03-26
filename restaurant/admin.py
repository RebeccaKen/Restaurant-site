from django.contrib import admin
from .models import Menu, MenuItem, Reservation, Order, Customer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Menu)
class MenuAdmin(SummernoteModelAdmin):

    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    summernote_fields = ('content',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'created_on')
    list_filter = ('description', 'name')
    search_fields = ('name', 'allegen', 'description')



def approve_reservations(modeladmin, request, queryset):
    queryset.update(is_approved=True)
    approve_reservations.short_description = "Reservation Approved"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('name', 'number_of_guests', 'date', 'phone', 'email')
    list_filter = ('name', 'date')
    search_fields = ('name', 'phone', 'email')
    actions = [approve_reservations]
    
    



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('name', 'reservation', 'order_date')
    list_filter = ('name', 'order_date')
    search_fields = ('name', 'phone', 'email')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'email', 'address')
    list_filter = ('name', 'phone')
    search_fields = ('name', 'phone')



