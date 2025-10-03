from django.shortcuts import render
from django.http import Http404

# Fake announcements data (later you can replace with models)
announcements_data = [
    {"id": 1, "title": "First Announcement", "content": "This is the detailed content of the first announcement. It contains more than 100 characters so you can test the Read more/Show less feature in the detail page."},
    {"id": 2, "title": "Second Announcement", "content": "This is the second announcement. It also has some extra text to check the toggle functionality in the detail template."},
]

def announcement_list(request):
    return render(request, "announcements/list.html", {"announcements": announcements_data})

def announcement_detail(request, id):
    # Find announcement by id
    announcement = next((a for a in announcements_data if a["id"] == id), None)
    if not announcement:
        raise Http404("Announcement not found")
    return render(request, "announcements/detail.html", {"announcement": announcement})
