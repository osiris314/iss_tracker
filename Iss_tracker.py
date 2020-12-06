import ISS_Info
from countries import *
import time
import os
from geopy.geocoders import Nominatim


while True:
    location = ISS_Info.iss_current_loc()
    lat = location['iss_position']['latitude']
    lon = location['iss_position']['longitude']
    try:
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.reverse(lat+","+lon)
        os.system('cls')
        print("Position:  latitude: {}, longitude: {}".format(lat,lon))
        print(location)

    except:
        os.system('cls')
        print("Position:  latitude: {}, longitude: {}".format(lat,lon))
        print('International waters')