from django.urls import path

from .views import NoteCreateView, NoteListView


urlpatterns = [
    path(
        '',
        NoteListView.as_view(),
        name='notes',
    ),
    path(
        'new/',
        NoteCreateView.as_view(),
        name='create_note',
    ),
]
