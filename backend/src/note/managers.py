from django.db import models


class RealManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted='False')

    def hard_delete(self):
        for item in self.all():
            item.hard_delete()
