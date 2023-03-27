from django.urls import path
from .views import HomePageView, MenuListView, TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu_list'),
]