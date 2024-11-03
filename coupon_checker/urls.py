from django.contrib import admin
from django.urls import path, include
from .views import WebsiteListView


urlpatterns = [
    path("", WebsiteListView.as_view())
]
