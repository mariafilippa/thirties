import csv

from django.core.management.base import BaseCommand

from ...models import UserMapping


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_path")

    def handle(self, *args, **options):
        with open(options['file_path']) as file:
            rows = csv.reader(file)
            next(rows, None)

            for row in rows:
                UserMapping.objects.update_or_create(
                    user_hash=row[0],
                    begin_time=row[1],
                    latitube=row[2],
                    month=row[3],
                    location=row[4],
                    label=row[5]
                )
