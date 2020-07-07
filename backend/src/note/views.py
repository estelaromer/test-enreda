from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note, User
from .serializers import (
    NewNoteSerializer,
    NoteSerializer,
    UserSerializer
)

from .services import get_user_by_email


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
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request, format=None):
        serializer = NewNoteSerializer(data=request.data)
        print(request.FILES.get('attached_file'))
        file_obj = request.FILES.get('attached_file')

        if not serializer.is_valid():
            print("NO VALIDO!")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = get_user_by_email(serializer.validated_data['user_email'])

        if not user:
            err = {'user': 'El usuario no existe o no se encuentra activo'}
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        if not file_obj:
            Note.objects.create(
                end_date=serializer.validated_data['end_date'],
                note=serializer.validated_data['note'],
                user=user,
                task=serializer.validated_data['task'],
                tag=serializer.validated_data['tag']
            )

        Note.objects.create(
            end_date=serializer.validated_data['end_date'],
            note=serializer.validated_data['note'],
            attached_file=file_obj,
            user=user,
            task=serializer.validated_data['task'],
            tag=serializer.validated_data.get('tag', None)
        )

        return Response(status=status.HTTP_201_CREATED)


class NoteRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    RETRIEVE/DESTROY a note
    """
    serializer_class = NoteSerializer
    queryset = Note.objects.get_active_user_notes()


class UserListView(ListAPIView):
    """
    GET active users ordered by email
    """
    serializer_class = UserSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = ('user__email', )

    def get_queryset(self):
        return User.objects.get_active()
