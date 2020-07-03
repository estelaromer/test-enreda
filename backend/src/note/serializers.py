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

from django.utils.timezone import make_aware

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

    def validate_end_date(self, value):
        if value <= make_aware(datetime.now()):
            raise ValidationError("La fecha final debe ser mayor a la actual")

        return value

    def validate_note(self, value):
        if len(value) < 1:
            raise ValidationError("El mensaje de la nota no puede estar vacío")

        return value
