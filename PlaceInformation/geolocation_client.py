# Kristi LaVigne
# CSCI 236
# 02/20/2021
# Program 02 - DNA
# hours: 2
# Grade Version - A
# major problems: none
# status of the program - compiles and runs
# ____________________________________________________________

from geolocation import GeoLocation


class GeolocationClient:
    stash = GeoLocation(34.988889, -106.614444)
    studio = GeoLocation(34.989978, -106.614357)
    fbi = GeoLocation(35.131281, -106.61263)

    print("the stash is at", stash.__str__())
    print("ABQ studio is at", studio.__str__())
    print("FBI building is at", fbi.__str__())

    stash_to_studio = stash.distance_from(studio)
    stash_to_fbi = stash.distance_from(fbi)

    print("distance in miles between:")
    print("    stash//studio = ", stash_to_studio)
    print("    stash/fbi     = ", stash_to_fbi)
