# Kristi LaVigne
# CSCI 236
# 02/20/2021
# Program 02 - DNA
# hours: 2
# Grade Version - A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

from geolocation import *

class PlaceInformation:
    def __init__(self, name, address, tag, latitude, longitude):
        self.__name = str(name)
        self.__address = str(address)
        self.__tag = str(tag)
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)
        self.__location = GeoLocation(latitude, longitude)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tag(self):
        return self.__tag

    def __str__(self):
        return "name: " + str(self.__name) + ", address: " + str(self.__address) + ", tag: " + str(self.__tag) + ", " + str(self.__location)

    def get_location(self):
        return self.__location

    def distance_from(self, spot): # spot is a GeoLocation object
        return self.__location.distance_from(spot)