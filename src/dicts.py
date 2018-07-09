# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
    {
        "lat": 42,
        "lon": 17,
        "name": "hobbiton"
    },
    {
        "lat": 13,
        "lon": 2,
        "name": "isengard"
    },
    {
        "lat": 54,
        "lon": 13,
        "name": "mordor"
    }
]

# Write a loop that prints out all the field values for all the waypoints
for w in waypoints:
    print(w['name'], w['lat'], w['lon'])