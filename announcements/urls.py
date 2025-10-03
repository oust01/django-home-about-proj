from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('announcements/', views.announcement_list, name='announcement_list'),  # list page
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),  # detail page
]
