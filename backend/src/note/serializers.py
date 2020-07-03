from rest_framework.serializers import ModelSerializer, SerializerMethodField

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
