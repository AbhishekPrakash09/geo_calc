from .documents import LocationDocument
from django_elasticsearch_dsl import Index
from .models import Location
from googlemaps import Client
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

gmaps = Client(key=settings.GOOGLE_API_KEY)

def search_location(query):

    print(query)
    search = LocationDocument.search().query("match", formatted_address=query)
    results = search.execute()

    if results:
        logger.info('found existing data in elasticsearch index')
        location = results[0]
        return {
            'formatted_address': location.formatted_address,
            'latitude': location.latitude,
            'longitude': location.longitude,
        }
    else:
        logger.info("querying google maps api")
        geocode_result = gmaps.geocode(query)
        
        if geocode_result:
            formatted_address = geocode_result[0]['formatted_address']
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']

            new_location, created = Location.objects.get_or_create(
                formatted_address=formatted_address,
                defaults={
                    'latitude': latitude,
                    'longitude': longitude
                }
            )

            if created: 
                LocationDocument().update(new_location)
                logger.info('creating new document in elasticsearch index')

            return {
                'formatted_address': formatted_address,
                'latitude': latitude,
                'longitude': longitude,
            }
        else:
            return None