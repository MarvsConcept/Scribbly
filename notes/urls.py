from django.urls import path
from . import views
from .views import NoteListView


urlpatterns = [
    path('', NoteListView.as_view(), name='home'),
]
