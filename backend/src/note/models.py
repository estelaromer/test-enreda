from django.db import models

from .managers import NoteManager, RealManager


class User(models.Model):
    """User model definition"""
    name = models.CharField(max_length=30)
    email = models.EmailField()
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    objects = RealManager()

    def __str__(self):
        return "{}, {}".format(self.name, self.email)

    def delete(self):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super(User, self).delete()


class Tag(models.Model):
    """Tag model definition"""
    tag_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return "{}".format(self.tag_name)


class Note(models.Model):
    """Note model definition"""
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    note = models.TextField()
    attached_file = models.FileField(null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    task = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        related_name='notes'
    )
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['user', 'end_date']

    objects = NoteManager()

    def __str__(self):
        return "{}, {}, {}".format(self.note, self.user, self.end_date)

    def delete(self):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super(Note, self).delete()
