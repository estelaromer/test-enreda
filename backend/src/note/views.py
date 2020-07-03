from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note
from .serializers import NewNoteSerializer, NoteSerializer
from .services import get_user_by_id


class NoteListView(ListAPIView):
    """
    GET notes ordered by user and end date
    """
    serializer_class = NoteSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = ('user__email', 'end_date')

    def get_queryset(self):
        return Note.objects.get_active_user_notes()


class NoteCreateView(APIView):
    """
    POST a new note
    """
    def post(self, request, format=None):
        serializer = NewNoteSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_by_id(serializer.validated_data['user_id'])

        if not user:
            err = {'user': 'El usuario no existe o no se encuentra activo'}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        note = Note.objects.create(
            end_date=serializer.validated_data['end_date'],
            note=serializer.validated_data['note'],
            user=user,
            task=serializer.validated_data['task']
        )

        if not note:
            err = {'note': 'Error guardando la nota'}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
