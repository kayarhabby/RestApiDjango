from django.core.management import BaseCommand
from faker import Faker
from RestApi.models import Author, Book, City, RoadSegment, Road
from django.contrib.gis.geos import Point
from random import randint, choice

class Command(BaseCommand):
    help = 'Populate database'

    def add_arguments(self, parser):
        parser.add_argument('--reset', action='store_true', help='Reset the data before populating')

    def handle(self, *args, **options):
        fake = Faker()

        if options['reset']:
            Author.objects.all().delete()
            Book.objects.all().delete()
            RoadSegment.objects.all().delete()
            Road.objects.all().delete()
            City.objects.all().delete()
            self.stdout.write(self.style.WARNING("Database reset completed."))

        # Create authors
        for _ in range(20):
            author = Author.objects.create(
                name=fake.name(),
                email=fake.email(),
                bio=fake.text()
            )
            self.stdout.write(self.style.SUCCESS(f'Created author: {author.name}'))

        # Create books
        authors = Author.objects.all()
        for _ in range(20):
            book = Book.objects.create(
                title=fake.sentence(),
                author=choice(authors),
                published_date=fake.date(),
                isbn=str(fake.unique.random_number(digits=13, fix_len=True))
            )
            self.stdout.write(self.style.SUCCESS(f'Created book: {book.title}'))

        # Create cities
        for _ in range(10):
            lon = float(fake.longitude())
            lat = float(fake.latitude())
            city = City.objects.create(
                name=fake.city(),
                population=str(randint(1000, 1000000)),
                location=Point(lon, lat)
            )
            self.stdout.write(self.style.SUCCESS(f'Created city: {city.name}'))

        # Create roads and road segments
        cities = City.objects.all()
        for i in range(10):
            road = Road.objects.create(
                name=f"Route {i + 1}",
                geometry=fake_line_geometry()
            )
            road_segment = RoadSegment.objects.create(
                road=road,
                start_km=randint(0, 100),
                end_km=randint(101, 200),
                status=choice(["good", "works", "slow"])
            )
            self.stdout.write(self.style.SUCCESS(
                f'Created road segment: {road_segment.road.name} [{road_segment.start_km} km → {road_segment.end_km} km] - {road_segment.status}'
            ))


# Helper to generate LineString
def fake_line_geometry():
    from django.contrib.gis.geos import LineString
    fake = Faker()
    points = [(float(fake.longitude()), float(fake.latitude())) for _ in range(2)]
    return LineString(*points)
