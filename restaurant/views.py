from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Menu, MenuItem, Reservation, Customer
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Feedback
from django.contrib import messages
from .forms import FeedbackForm 
from django.forms import ModelForm
from allauth.account.forms import UserForm
from django.views.generic.edit import FormView
from .models import Menu, MenuItem

#Views for restaurant website

class HomePageView(TemplateView):
    template_name = 'home.html'

class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = MenuItem.objects.all()
        return context


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = 'reservation_detail.html'
    context_object_name = 'reservation'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
        else:
            queryset = queryset.none()
        return queryset


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = 'reservation_create.html'
    fields = ['name', 'email', 'phone', 'number_of_guests', 'reservation_time', 'reservation_date', 'notes',]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def __str__(self):
        return f'{self.user.username} - Reservation #{self.id}'

    def get_success_url(self):
        messages.success(self.request, 'Thank you for your reservation!')
        return reverse_lazy('reservation_list')


class ReservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = self.get_queryset()
        return context

class ReservationEditView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = 'reservation_edit.html'
    fields = ['name', 'number_of_guests', 'email', 'phone', 'reservation_time', 'reservation_date', 'notes', 'is_approved']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Reservation, id=id, user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'Your reservation has been edited!')
        return reverse_lazy('home')


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
    fields = ['name', 'email', 'comments', 'rating']
    paginate_by = 5
    submitted = False

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.approved = False
            feedback.save()
            self.submitted = True
        else:
            self.submitted = False
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        context['submitted'] = getattr(self, 'submitted', False)
        return context

