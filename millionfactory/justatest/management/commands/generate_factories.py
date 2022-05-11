import random

from django.contrib.gis.geos import GEOSGeometry, Point
from django.core.management.base import BaseCommand, CommandError
from justatest.models import Factory

RANDOM_LAT_MAX = 25.298401
RANDOM_LAT_MIN = 21.896900
RANDOM_LNG_MAX = 122.007164
RANDOM_LNG_MIN = 120.035141


class Command(BaseCommand):
    help = 'Generate factories'

    def add_arguments(self, parser):
        parser.add_argument('factory_number', nargs='+', type=int)

    def handle(self, *args, **options):

        total_factories = Factory.objects.count()

        while True:
            geometry_location = GEOSGeometry(
                Point(
                    random.uniform(RANDOM_LNG_MIN, RANDOM_LNG_MAX),
                    random.uniform(RANDOM_LAT_MIN, RANDOM_LAT_MAX),
                ),
                srid=4326,
            )
            Factory.objects.create(location=geometry_location)
            total_factories += 1
            current_percentage = total_factories / options['factory_number'][0]
            if total_factories % 200 == 0:
                print_stdout(
                    self,
                    "".join(
                        [
                            str(total_factories),
                            f"({current_percentage:.2%})",
                        ]
                    ),
                )
            if total_factories == options['factory_number'][0]:
                break


def print_stdout(cls, stdout_content):
    cls.stdout.write(
        "\n".join(
            [
                stdout_content,
                "",
            ]
        )
    )
