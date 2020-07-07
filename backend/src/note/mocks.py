from datetime import datetime
from faker import Faker
from faker.providers import lorem
from model_bakery import baker

from django.utils.timezone import make_aware

fake = Faker()
fake.add_provider(lorem)


def generate_mock_data():
    user = baker.make(
        'note.user',
        name='Marta Barros',
        email='martabarros@example.com'
    )
    baker.make(
        'note.note',
        end_date=make_aware(datetime(2020, 7, 15, 18, 0, 0)),
        note=fake.text(),
        user=user,
        task=False
    )
    baker.make(
        'note.note',
        end_date=make_aware(datetime(2020, 7, 17, 18, 0, 0)),
        note=fake.text(),
        user=user,
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
    )
