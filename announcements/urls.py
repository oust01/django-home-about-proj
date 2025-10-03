from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('announcement/', views.announcement_list, name='announcement_list'),
    path('announcements/<int:id>/', views.announcement_detail, name='announcement_detail'),
]
