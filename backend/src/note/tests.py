from datetime import datetime
from faker import Faker
from faker.providers import lorem
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from django.utils.timezone import make_aware

from .models import User, Note

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


class PostNoteTest(APITestCase):
    """
    POST a note
    """
    def setUp(self):
        self.active_user = baker.make(
            'note.user',
            name='Marta Barros',
            email='martabarros@example.com'
        )
        self.inactive_user = baker.make(
            'note.user',
            name='Sara Merino',
            email='saramerino@example.com',
            deleted=True
        )

    def test_post_note_without_tag_valid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime(2020, 7, 13, 20, 0, 0)),
            'note': fake.text(),
            'user_id': self.active_user.id,
            'task': False
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_note_with_tag_valid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime(2020, 7, 13, 20, 0, 0)),
            'note': fake.text(),
            'user_id': self.active_user.id,
            'task': False,
            'tag': 'Factura'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_note_tag_invalid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime(2020, 7, 13, 20, 0, 0)),
            'note': fake.text(),
            'user_id': self.active_user.id,
            'task': False,
            'tag': 'Vamos a crear una cadena que sea más larga de treinta caracteres'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_note_end_date_invalid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime.now()),
            'note': fake.text(),
            'user_id': self.active_user.id,
            'task': False
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_note_note_invalid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime(2020, 7, 13, 20, 0, 0)),
            'note': None,
            'user_id': self.active_user.id,
            'task': False
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_note_user_invalid(self):
        url = reverse('create_note')
        data = {
            'end_date': make_aware(datetime(2020, 7, 13, 20, 0, 0)),
            'note': fake.text(),
            'user_id': self.inactive_user.id,
            'task': False
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        Note.objects.hard_delete()
        User.objects.hard_delete()
