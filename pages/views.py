from django.views.generic import ListView
from .models import Contact


class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact
