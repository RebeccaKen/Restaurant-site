from django.urls import path
from .views import HomePageView, MenuListView, TemplateView
from .views import ReservationCreateView, FeedbackListView
from .views import ReservationEditView, ReservationDeleteView
from .views import reservation_detail


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('reservation/create', ReservationCreateView.as_view(), name='reservation'),
    path('reservation/<int:reservation_id>/', reservation_detail, name='reservation_detail'),
    path('reservation/<int:pk>/edit/', ReservationEditView.as_view(), name='reservation_edit'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
    path('feedback/', FeedbackListView.as_view(), name='feedback'),
]