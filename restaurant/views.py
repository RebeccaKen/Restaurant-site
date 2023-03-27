from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView, TemplateView
from .models import Menu, MenuItem, Reservation, Order, Customer
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView



# Views for restaurant website
def get_restaurant_list(request):
    return render(request, 'restaurant/restaurant_list.html')


class HomePageView(TemplateView):
    template_name = 'home.html'


class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'


class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = 'menu_item_form.html'
    fields = ['name', 'slug', 'description', 'allergens', 'price', 'menu']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



