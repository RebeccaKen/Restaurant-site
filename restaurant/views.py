from django.shortcuts import render
from django.views import generic

# Create your views here.
def get_restaurant_list(request):
    return render(request, 'restaurant/restaurant_list.html')




