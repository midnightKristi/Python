# Kristi LaVigne
# CSCI 236
# 02/20/2021
# Program 02 - DNA
# hours: 2
# Grade Version - A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

# This class stores information about a location on Earth.  Locations are
# specified using latitude and longitude.  The class includes a method for
# computing the distance between two locations.

from math import *

RADIUS = 3963.1676  # Earth radius in miles


class GeoLocation:

    # constructs a geo location object with given latitude and longitude
    def __init__(self, latitude, longitude):
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)

    # returns the latitude of this geo location
    def get_latitude(self):
        return self.__latitude

    # returns the longitude of this geo location
    def get_longitude(self):
        return self.__longitude

    # returns a string representation of this geo location
    def __str__(self):
        return "latitude: " + str(self.__latitude) + ", longitude: " + str(self.__longitude)

    # WRITE THIS METHOD FOR AN A
    # returns the distance in miles between this geo location and the given
    # other geo location
    # YOU NEED TO WRITE THIS METHOD; EMAIL ME IF YOU CANNOT FIGURE IT OUT; YOUR GRADE WILL BE LOWER
    def distance_from(self, other):
        dLat = radians(other.get_latitude() - self.__latitude)
        dLon = radians(other.get_longitude() - self.__longitude)
        lat1 = radians(self.__latitude)
        lat2 = radians(other.get_longitude())
        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(abs(a)))
        answer = RADIUS * c
        return answer
