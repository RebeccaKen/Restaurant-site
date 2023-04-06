from django.contrib import admin
from .models import Menu, MenuItem, Reservation, Feedback, Customer
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


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('name', 'reservation_date', 'reservation_time', 'phone')
    list_display = ('email', 'is_approved')
    list_filter = ('name', 'reservation_date',)
    list_filter = ('reservation_time', 'is_approved')
    search_fields = ('name', 'phone', 'email')
    actions = ['approve_reservation']

    def approve_reservation(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'date', 'rating', 'approved')
    list_filter = ('approved', 'date', 'rating')
    search_fields = ('name', 'email', 'comments')
    actions = ['approve_feedback']

    def approve_feedback(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'email', 'address')
    list_filter = ('name', 'phone')
    search_fields = ('name', 'phone')



