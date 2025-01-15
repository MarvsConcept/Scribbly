from django.urls import path
from . import views
from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    UserNoteListView,
)
urlpatterns = [
    path('', NoteListView.as_view(), name='home'),
    path('user/<str:username>/', UserNoteListView.as_view(), name='user-note'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),

]
