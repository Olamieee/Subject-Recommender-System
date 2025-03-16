from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset migrations'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Reset the Django migrations table
            cursor.execute("DELETE FROM django_migrations WHERE app = 'recommenderApp';")
            self.stdout.write(self.style.SUCCESS('Successfully reset migrations'))