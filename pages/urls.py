from django.urls import path
from .views import HomePageView, ContactDetailView


urlpatterns = [
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact_detail'),
    path('', HomePageView.as_view(), name='homepage'),
]
