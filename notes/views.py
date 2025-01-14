from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Notes
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
    paginate_by = '5'


class UserNoteListView(ListView):
    model = Notes
    template_name = 'notes/user_notes.html'
    context_object_name = 'notes'
    paginate_by = '5'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Notes.objects.filter(author=user).order_by('-date_posted')

class NoteDetailView(DetailView):
    model = Notes

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False