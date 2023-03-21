from django.shortcuts import render

# Create your views here.
def get_restaurant_list(request):
    return render(request, 'restaurant/restaurant_list.html')
