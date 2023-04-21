from django.urls import path
from .views import HomePageView, MenuListView, TemplateView
from .views import ReservationCreateView, FeedbackListView
from .views import ReservationEditView, ReservationDeleteView
from .views import ReservationDetailView, ReservationListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu_list'),
    path('reservation/create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservation_user/', ReservationListView.as_view(), name='reservation_user'),
    path('reservation/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservation/<int:pk>/edit/', ReservationEditView.as_view(), name='reservation_edit'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
    path('feedback/', FeedbackListView.as_view(), name='feedback'),
]