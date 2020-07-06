from datetime import datetime

from rest_framework.serializers import (
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    ValidationError,
)

from django.utils.timezone import make_aware

from .models import Note, User


# class NoteSerializer(ModelSerializer):
#     user_email = SerializerMethodField()
#     user_name = SerializerMethodField()

#     class Meta:
#         model = Note
#         fields = (
#             'id',
#             'date',
#             'end_date',
#             'note',
#             'user_email',
#             'user_name',
#             'task',
#             'tag'
#         )

#     def get_user_email(self, obj):
#         return obj.user.email

#     def get_user_name(self, obj):
#         return obj.user.name


class NoteSerializer(ModelSerializer):
    user_id = SerializerMethodField()
    user_email = SerializerMethodField()
    user_name = SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            'id',
            'date',
            'end_date',
            'note',
            'user_id',
            'user_email',
            'user_name',
            'task',
            'tag'
        )

    def get_user_id(self, obj):
        return obj.user.id

    def get_user_email(self, obj):
        return obj.user.email

    def get_user_name(self, obj):
        return obj.user.name

    def validate_end_date(self, value):
        if value <= make_aware(datetime.now()):
            raise ValidationError("La fecha final debe ser mayor a la actual")

        return value

    def validate_note(self, value):
        if not isinstance(value, str):
            raise ValidationError("El mensaje no es una cadena")
        if len(value) < 1:
            raise ValidationError("El mensaje de la nota no puede estar vacío")

        return value

    def validate_tag(self, value):
        if value and len(value) > 30:
            raise ValidationError("La tag no debe ocupar más de 30 caracteres")

        return value


class NewNoteSerializer(Serializer):
    end_date = DateTimeField(format="%Y-%m-%d %H:%M:%S")
    note = CharField(min_length=1)
    user_email = EmailField()
    task = BooleanField()
    tag = CharField(required=False)

    def validate_end_date(self, value):
        if value <= make_aware(datetime.now()):
            raise ValidationError("La fecha final debe ser mayor a la actual")

        return value

    def validate_note(self, value):
        if len(value) < 1:
            raise ValidationError("El mensaje de la nota no puede estar vacío")

        return value

    def validate_tag(self, value):
        if len(value) > 30:
            raise ValidationError("La tag no debe ocupar más de 30 caracteres")

        return value


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email'
        )
