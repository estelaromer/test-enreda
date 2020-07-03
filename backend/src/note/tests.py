from datetime import datetime
from faker import Faker
from faker.providers import lorem
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from django.utils.timezone import make_aware

from .models import User, Tag, Note

fake = Faker()
fake.add_provider(lorem)


class GetNoteTest(APITestCase):
    """
    GET Notes
    """
    def setUp(self):
        self.active_notes_counter = 3
        self.notes = [
            baker.make(
                'note.note',
                end_date=make_aware(datetime(2020, 7, 15, 18, 0, 0)),
                note=fake.text(),
                user=baker.make(
                    'note.user',
                    name='Marta Barros',
                    email='martabarros@example.com'
                ),
                task=False
            ),
            baker.make(
                'note.note',
                end_date=make_aware(datetime(2020, 7, 17, 18, 0, 0)),
                note=fake.text(),
                user=baker.make(
                    'note.user',
                    name='Marta Barros',
                    email='martabarros@example.com'
                ),
                task=False
            ),
            baker.make(
                'note.note',
                end_date=make_aware(datetime(2020, 7, 20, 18, 0, 0)),
                note=fake.text(),
                user=baker.make(
                    'note.user',
                    name='Luis LLanos',
                    email='luisllanos@example.com'
                ),
                task=True
            ),
            baker.make(
                'note.note',
                end_date=make_aware(datetime(2020, 7, 22, 18, 0, 0)),
                note=fake.text(),
                user=baker.make(
                    'note.user',
                    name='Pablo Amaro',
                    email='pabloamaro@example.com'
                ),
                task=False,
                deleted=True
            ),
            baker.make(
                'note.note',
                end_date=make_aware(datetime(2020, 7, 25, 18, 0, 0)),
                note=fake.text(),
                user=baker.make(
                    'note.user',
                    name='Sara Merino',
                    email='saramerino@example.com',
                    deleted=True
                ),
                task=False
            ),
        ]

    def test_get_notes_valid(self):
        url = reverse('notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.active_notes_counter)

    def tearDown(self):
        Note.objects.hard_delete()
        User.objects.hard_delete()
