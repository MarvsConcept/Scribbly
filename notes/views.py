from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes
from django.views.generic import ListView

# Create your views here.

# def home(request):
#     context = {
#         'notes': Notes.objects.all()
#         }
#     return render(request, 'notes/home.html', context )

class NoteListView(ListView):
    model = Notes
    template_name = 'notes/home.html'
    context_object_name = 'notes'
    ordering = ['-date_posted']