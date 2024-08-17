from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Location

# Define the index in Elasticsearch
location_index = Index('locations')

location_index.settings(
    number_of_shards=1,
    number_of_replicas=1,
)

@registry.register_document
@location_index.document
class LocationDocument(Document):
    class Index:
        name = 'locations'
    
    class Django:
        model = Location
        fields = [
            'formatted_address',
            'latitude',
            'longitude',
        ]
