from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Location

@registry.register_document
class LocationDocument(Document):
    class Index:
        name = 'locations'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Location
        fields = [
            'formatted_address',
            'latitude',
            'longitude',
        ]
