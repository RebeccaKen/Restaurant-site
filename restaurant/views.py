from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Menu, MenuItem, Reservation, Order, Customer
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView



#Views for restaurant website

class HomePageView(TemplateView):
    template_name = 'home.html'


class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'reservation_form.html'
    fields = ['name', 'email', 'phone', 'date', 'number_of_guests', 'notes',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'reservation_form.html'
    fields = ['name', 'email', 'phone', 'date', 'number_of_guests', 'notes']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_confirm_delete.html'
    success_url = reverse_lazy('reservation_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


