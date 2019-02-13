import time
import grovepi
import dweepy
dweet_key= "LauraPi"
# Connect the Grove Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
potentiometer = 0

# Connect the LED to digital port D5
# SIG,NC,VCC,GND
led = 5

grovepi.pinMode(potentiometer,"INPUT")
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

def getSensor():
    sensor = grovepi.analogRead(potentiometer)
    print (sensor)
    return sensor
def getVoltage():
    voltage = round((float)(grovepi.analogRead(potentiometer)) * adc_ref / 1023, 2)
    print(voltage)
    return voltage
def getDegrees():
    degrees = round((round((float)(grovepi.analogRead(potentiometer)) * adc_ref / 1023, 2) * full_angle) / grove_vcc, 2)
    print (degrees)
    return degrees
def getBrightness():
    brightness = int(round((round((float)(grovepi.analogRead(potentiometer)) * adc_ref / 1023, 2) * full_angle)/ full_angle * 255))
    print (brightness)
    return brightness
def post(dic):
    thing = 'LauraPi'
    print (dweepy.dweet_for(thing,dic))
    
def getReadings():
    dict = {}
    dict["sensor"] = getSensor();
    time.sleep(1)
    dict["voltage"] = getVoltage();
    time.sleep(1)
    dict["degrees"] = getDegrees();
    time.sleep(1)
    dict["brightness"] = getBrightness();
    return dict

while True:
    dict = getReadings();
    time.sleep(1)
    post(dict)
