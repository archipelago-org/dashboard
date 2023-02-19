from archipelago.models.location import LocationResponse, Location

DUMMY_LAT_1 = -27.5598
DUMMY_LON_1 = 151.9507
DUMMY_LAT_2 = -24.8661
DUMMY_LON_2 = 152.3489
DUMMY_LAT_3 = -32.0518
DUMMY_LON_3 = 115.7551
DUMMY_WEIGHT_1 = 78.23
DUMMY_WEIGHT_2 = 18.12
DUMMY_WEIGHT_3 = 45.23
DUMMY_PRODUCT = "Floatation Disks"


def get_location():
    location_1 = Location(
        latitude=DUMMY_LAT_1,
        longitude=DUMMY_LON_1,
        weight=DUMMY_WEIGHT_1,
        product=DUMMY_PRODUCT
    )
    location_2 = Location(
        latitude=DUMMY_LAT_2,
        longitude=DUMMY_LON_2,
        weight=DUMMY_WEIGHT_2,
        product=DUMMY_PRODUCT
    )
    location_3 = Location(
        latitude=DUMMY_LAT_3,
        longitude=DUMMY_LON_3,
        weight=DUMMY_WEIGHT_3,
        product=DUMMY_PRODUCT
    )
    response = LocationResponse(locations=[location_1, location_2, location_3])
    return response
