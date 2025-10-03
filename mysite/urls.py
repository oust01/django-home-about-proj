from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", lambda request: render(request, "home.html"), name="home"),  # Home page
    path("announcements/", include("announcements.urls")),  # Announcements list & detail
]
