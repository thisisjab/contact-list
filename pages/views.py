from django.views.generic import ListView, DetailView
from .models import Contact


class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact


class ContactDetailView(DetailView):
    template_name = 'contact.html'
    model = Contact
