from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Menu, MenuItem, Reservation, Customer
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Feedback
from django.contrib import messages



#Views for restaurant website

class HomePageView(TemplateView):
    template_name = 'home.html'


class MenuListView(ListView):
    model = Menu
    template_name = 'menu.html'
    context_object_name = 'menus'


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'reservation.html'
    fields = ['name', 'email', 'phone', 'date', 'notes',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Thank you for your reservation!')
        return reverse_lazy('home')


class ReservationEditView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'reservation_edit.html'
    fields = ['name', 'email', 'phone', 'date', 'notes']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation
    template_name = 'reservation_delete.html'
    success_url = reverse_lazy('reservation_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved=True)
        return queryset



