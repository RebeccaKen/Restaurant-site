from django.urls import path
from .views import HomePageView, MenuListView, TemplateView, ReservationEditView
from .views import ReservationCreateView, FeedbackListView, ReservationDeleteView
from .views import AccountSettingsView, EditAccountView, DeleteAccountView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu/', MenuListView.as_view(), name='menu'),
    path('reservation/create', ReservationCreateView.as_view(), name='reservation'),
    path('reservation/<int:pk>/update/', ReservationEditView.as_view(), name='reservation_edit'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
    path('feedback/', FeedbackListView.as_view(), name='feedback'),
    path('account/settings/', AccountSettingsView.as_view(), name='account_settings'),
    path('account/edit/', EditAccountView.as_view(), name='edit_account'),
    path('account/delete/', DeleteAccountView.as_view(), name='delete_account'),
]