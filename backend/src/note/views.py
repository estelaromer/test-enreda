from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .models import Note
from .serializers import NoteSerializer


class NoteListView(ListAPIView):
    """
    GET notes ordered by user and end date
    """
    serializer_class = NoteSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = ('user__email', 'end_date')

    def get_queryset(self):
        return Note.objects.get_active_user_notes()
