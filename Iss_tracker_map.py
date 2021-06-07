import ISS_Info
import countries
import turtle
import time
import os
from geopy.geocoders import Nominatim

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('world_map.png')
screen.register_shape('iss_icon.gif')

iss = turtle.Turtle()
turtle.title('ISS Tracker')
iss.shape('iss_icon.gif')
iss.penup()

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
        iss.goto(float(lon),float(lat))
    except:
        os.system('cls')
        print("Position:  latitude: {}, longitude: {}".format(lat,lon))
        print('International waters')
        iss.goto(float(lon),float(lat))
