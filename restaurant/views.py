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
from .forms import AccountSettingsForm, EditAccountForm
from django.views.generic.edit import FormView

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
    fields = ['name', 'email', 'phone', 'number_of_guests', 'date', 'notes',]

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


class AccountSettingsView(LoginRequiredMixin, FormView):
    template_name = 'account_settings.html'
    form_class = AccountSettingsForm
    success_url = reverse_lazy('account_settings')

    def form_valid(self, form):
        customer = get_object_or_404(Customer, user=self.request.user)
        customer.name = form.cleaned_data['name']
        customer.phone = form.cleaned_data['phone']
        customer.email = form.cleaned_data['email']
        customer.address = form.cleaned_data['address']
        customer.save()
        messages.success(self.request, 'Your account has been updated.')
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user.customer
        return kwargs


class EditAccountView(LoginRequiredMixin, FormView):
    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, user=request.user)
        form = AccountSettingsForm(instance=customer)
        return render(request, 'edit_account.html', {'form': form})

    def post(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, user=request.user)
        form = AccountSettingsForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('account_settings')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, 'edit_account.html', {'form': form})


class DeleteAccountView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'delete_account.html')

    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')

