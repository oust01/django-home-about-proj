from django.shortcuts import render
from django.http import HttpResponse

# Sample announcements data (later you can use models, but for now just simple list)
announcements = [
    {"id": 1, "title": "Welcome to our site", "content": "This is the very first announcement."},
    {"id": 2, "title": "Update Released", "content": "We have added new features today."},
    {"id": 3, "title": "Maintenance Notice", "content": "The site will be down for maintenance tomorrow night."},
]

def home(request):
    return render(request, "home.html")

def announcements_list(request):
    return render(request, "announcements/list.html", {"announcements": announcements})

def announcement_detail(request, id):
    announcement = next((a for a in announcements if a["id"] == id), None)
    return render(request, "announcements/detail.html", {"announcement": announcement})
