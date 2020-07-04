from django.urls import path

from .views import (
    NoteCreateView,
    NoteListView,
    NoteRetrieveUpdateDestroyView,
)

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
    path(
        '<int:pk>/',
        NoteRetrieveUpdateDestroyView.as_view(),
        name='note',
    ),
]
