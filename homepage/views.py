from django.shortcuts import render
from django.views.generic import ListView
import requests

# Create your views here.
class HomeListView(ListView):
    template_name = 'dashboard.html'
    context_object_name = 'websites'

    def get_queryset(self):
        response = requests.get('http://127.0.0.1:8000/api/websites/')
        if response.status_code == 200:
            return response.json()
        return []