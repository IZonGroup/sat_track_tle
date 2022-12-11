#In this example, the lines variable contains the TLE data for the satellite, which is then loaded into a satellite object using the api.load.tle() method. The earth and topos objects are used to compute the satellite's position relative to the Earth. The time variable is set to a specific date and time, and the position variable is computed by calling the at() method on the topos object. Finally, the satellite's position is printed in kilometers which we will likelty change.

from skyfield import api

# Load TLE data for the satellite you want to track
lines = [
    '1 25544U 98067A   20281.79072380  .00002372  00000-0  43835-4 0  9990',
    '2 25544  51.6441  43.2383 0001939  35.3867  63.9087 15.49031723181745',
]
satellite = api.load.tle(*lines)

# Create a Skyfield Earth and Topos object
earth = api.EarthSatellite()
topos = satellite - earth

# Compute the satellite's position at a given time
ts = api.load.timescale()
time = ts.utc(2022, 12, 11, 12, 0, 0)
position = topos.at(time)

# Print the satellite's position. There are better options then using km for this
print(position.position.km)
