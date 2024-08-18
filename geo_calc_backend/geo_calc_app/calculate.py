import math

def calculate_distance(location1, location2):

    lat1, lon1 = float(location1['latitude']), float(location1['longitude'])
    lat2, lon2 = float(location2['latitude']), float(location2['longitude'])

 
    lat1, lon1 = math.radians(lat1), math.radians(lon1)
    lat2, lon2 = math.radians(lat2), math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Radius of the Earth in kilometers (mean radius)
    R = 6371.0

    distance = R * c

    distance = round(distance, 2)

    return distance