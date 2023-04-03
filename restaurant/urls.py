from django.urls import path
from .views import HomePageView, MenuListView, TemplateView, ReservationEditView
from .views import ReservationCreateView, FeedbackListView, ReservationDeleteView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('reservation/create', ReservationCreateView.as_view(), name='reservation'),
    path('reservation/<int:pk>/update/', ReservationEditView.as_view(), name='reservation_edit'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
    path('feedback/', FeedbackListView.as_view(), name='feedback'),
]