from django.db import models


class RealManager(models.Manager):
    def get_active(self):
        return self.all().filter(deleted='False')

    def hard_delete(self):
        for item in self.all():
            item.hard_delete()


class NoteManager(RealManager):
    def get_active_user_notes(self):
        return self.get_active().filter(user__deleted=False)
