from datetime import datetime

from rest_framework.serializers import (
    BooleanField,
    CharField,
    DateTimeField,
    IntegerField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    ValidationError,
)

from .models import Note


class NoteSerializer(ModelSerializer):
    user_email = SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            'id',
            'date',
            'end_date',
            'note',
            'user_email',
            'task',
        )

    def get_user_email(self, obj):
        return obj.user.email


class NewNoteSerializer(Serializer):
    end_date = DateTimeField(format="%Y-%m-%d %H:%M:%S")
    note = CharField(min_length=1)
    user_id = IntegerField()
    task = BooleanField()
