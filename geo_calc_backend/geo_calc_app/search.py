from .documents import LocationDocument
from .models import Location
from googlemaps import Client
from django.conf import settings

gmaps = Client(key=settings.GOOGLE_API_KEY)

def search_location(query):

    search = LocationDocument.search().query("match", formatted_address=query)
    results = search.execute()

    if results:
        location = results[0]
        return {
            'formatted_address': location.formatted_address,
            'latitude': location.latitude,
            'longitude': location.longitude,
        }
    else:
        geocode_result = gmaps.geocode(query)
        
        if geocode_result:
            formatted_address = geocode_result[0]['formatted_address']
            location = geocode_result[0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']

            new_location = Location.objects.create(
                formatted_address=formatted_address,
                latitude=latitude,
                longitude=longitude
            )

            new_location.save()

            return {
                'formatted_address': formatted_address,
                'latitude': latitude,
                'longitude': longitude,
            }
        else:
            return None