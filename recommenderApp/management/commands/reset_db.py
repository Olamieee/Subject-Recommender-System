from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the entire database'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Get all tables
            cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            """)
            tables = [row[0] for row in cursor.fetchall()]
            
            # Disable foreign key checks 
            cursor.execute("SET CONSTRAINTS ALL DEFERRED;")
            
            # Drop all tables
            for table in tables:
                if table != 'spatial_ref_sys':  # Don't drop PostGIS tables if present
                    cursor.execute(f'DROP TABLE IF EXISTS "{table}" CASCADE;')
            
            self.stdout.write(self.style.SUCCESS('Successfully dropped all tables'))