from django.urls import path
from .views import HomePageView, MenuListView, TemplateView, ReservationUpdateView, ReservationDeleteView
from .views import ReservationCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('reservation/create', ReservationCreateView.as_view(), name='reservation'),
    path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete')
]