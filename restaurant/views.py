from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Menu, MenuItem, Reservation, Order, Customer
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ContactForm
from .models import Contact



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


class ContactPageView(View):
    model = Contact
    template_name = contact.html

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(name=form.cleaned_data['name'], email=form.cleaned_data['email'], message=form.cleaned_data['message'])
            contact.save()
            subject = 'Contact form submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('contact_success')
        else:
            context = {'form': form}
            return render(request, self.template_name, context)
