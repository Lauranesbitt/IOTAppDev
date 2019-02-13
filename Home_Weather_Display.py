from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import dweepy
import fcntl,socket
dweet_key= "LauraPi"

dht_sensor_port = 3 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored sensor
#get the temperature readings

def getTemp():
    temp = dht(dht_sensor_port,dht_sensor_type)
    time.sleep(1)
    print(temp)
    return temp
#get the humidity readings
def getHum():
    hum = dht(dht_sensor_port,dht_sensor_type)
    time.sleep(1)
    print(hum)
    return hum

#once the readings are received publish them to dweet.io
def post(dic):
    thing = 'LauraPi'
    print (dweepy.dweet_for(thing,dic))

def getReadings():
    dict = {}
    dict["temp"] = getTemp();
    time.sleep(1)
    dict["hum"] = getHum();
    return dict

while True:
    dict = getReadings();
    time.sleep(1)
    post(dict)

	# wait some time before re-updating the LCD
sleep(0.05)
