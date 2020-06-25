from django.shortcuts import render
from .models import Project


def home(request):
    data = Project.objects.all()
    return render(request, 'webpages/home.html', {'projects':data})
    