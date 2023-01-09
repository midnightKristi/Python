# Kristi LaVigne
# CSCI 236
# 02/20/2021
# Program 02 - DNA
# hours: 2
# Grade Version - A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

# This program constructs several PlaceInformation objects and prints
# information about them and the distances between them and two locations
# (London and Kane Hall).  It is intended to be used to test whether the
# PlaceInformation class is implemented correctly.


from geolocation import *
from place_information import *


def main():
    data = [PlaceInformation("Mount Lemmon", "Tucson",
                             "tourist, park", 32.44380, -110.77134),
            PlaceInformation("Student Union Building", "University of Arizona campus",
                             "restaurant", 32.23262, -110.95206),
            PlaceInformation("Gould-Simpson Hall", "University of Arizona campus",
                             "university, ua", 32.22976, -110.95501)]

    london = GeoLocation(51.5112139, -0.1198244)
    old_main = GeoLocation(32.23189, -110.95342)

    for info in data:
        print("name    : " + info.get_name())
        print("address : " + info.get_address())
        print("tags    : " + info.get_tag())
        print("__str__ : " + str(info))
        print("London  : " + str(info.distance_from(london)))
        print("Old Main: " + str(info.distance_from(old_main)))
        print()


main()
