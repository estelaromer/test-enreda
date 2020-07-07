from django.core.management.base import BaseCommand
from ...mocks import generate_mock_data


class Command(BaseCommand):
    help = 'Populate database with mock data'

    def handle(self, *args, **options):
        generate_mock_data()
        self.stdout.write(self.style.SUCCESS('Database successfully populated'))
