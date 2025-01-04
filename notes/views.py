from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes

# Create your views here.

def home(request):
    context = {
        'notes': Notes.objects.all()
        }
    return render(request, 'notes/home.html', context )