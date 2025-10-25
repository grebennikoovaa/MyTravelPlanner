import os
import django
import sys

# Добавляем текущую директорию в Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from trips.models import Trip, Destination, TripDay, DayDestination
from django.utils import timezone

def create_rome_trip():
    User = get_user_model()
    
    # Используем существующего пользователя или создаем нового
    try:
        user = User.objects.get(username='testuser')
        print("✅ Found user testuser")
    except User.DoesNotExist:
        user = User.objects.create_user('testuser', 'test@example.com', 'testpass123')
        user.save()
        print("✅ Created user testuser")
    
    # Создаем путешествие
    trip = Trip.objects.create(
        title='Vacation in Rome',
        description='Unforgettable journey to Italy with visits to main attractions',
        start_date=timezone.now().date(),
        end_date=timezone.now().date() + timezone.timedelta(days=3),
        owner=user,
        privacy='public'
    )
    print("✅ Trip created")
    
    # Создаем дни (3 дня для 3-дневной поездки)
    days = []
    for i in range(3):
        day = TripDay.objects.create(
            trip=trip,
            date=trip.start_date + timezone.timedelta(days=i),
            day_number=i + 1
        )
        days.append(day)
    print(f"✅ Created {len(days)} days")
    
    # Создаем места (достопримечательности) - ТОЛЬКО 3 МЕСТА
    destinations_data = [
        {
            'name': 'Colosseum',
            'description': 'Ancient Roman amphitheater',
            'address': 'Piazza del Colosseo, 1',
            'city': 'Rome',
            'country': 'Italy',
            'category': 'landmark'
        },
        {
            'name': 'Vatican',
            'description': 'City-state and St. Peter\'s Basilica',
            'address': '00120 Vatican City',
            'city': 'Rome', 
            'country': 'Italy',
            'category': 'landmark'
        },
        {
            'name': 'Trevi Fountain',
            'description': 'Famous fountain where people throw coins',
            'address': 'Piazza di Trevi',
            'city': 'Rome',
            'country': 'Italy',
            'category': 'landmark'
        }
    ]
    
    created_destinations = []
    for dest in destinations_data:
        destination = Destination.objects.create(
            name=dest['name'],
            description=dest['description'],
            address=dest['address'],
            city=dest['city'],
            country=dest['country'],
            category=dest['category'],
            created_by=user
        )
        created_destinations.append(destination)
    print(f"✅ Created {len(created_destinations)} destinations")
    
    # Распределяем места по дням (по одному месту на день)
    DayDestination.objects.create(trip_day=days[0], destination=created_destinations[0], order=1)
    DayDestination.objects.create(trip_day=days[1], destination=created_destinations[1], order=1)
    DayDestination.objects.create(trip_day=days[2], destination=created_destinations[2], order=1)
    print("✅ Destinations assigned to days")
    
    print("\n TRIP SUCCESSFULLY CREATED!")
    print(f" Title: {trip.title}")
    print(f" Period: {trip.start_date} - {trip.end_date}")
    print(f" Owner: {user.username}")
    print(f" Days: {trip.days.count()}")
    print(f" Destinations: {len(created_destinations)}")
    print(f" View: http://127.0.0.1:8000/trips/{trip.id}/")

if __name__ == "__main__":
    create_rome_trip()