from django.urls import path
from .views import import_aircrafts, match_aircrafts_to_airlines

urlpatterns = [
    # ... другие маршруты ...
    path('import-aircrafts/', import_aircrafts, name='import_aircrafts'),
    path('match-aircrafts-to-airlines/', match_aircrafts_to_airlines, name='match_aircrafts_to_airlines'),
]