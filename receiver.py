import dweepy
import subprocess

for dweet in dweepy.listen_for_dweets_from('LauraPi'):
    for content in dweet:
        if content.find("hello "):
            subprocess.call(['python', 'led_blink.py'])
        elif content.find("moisture"):
            subprocess.call(['python', '/home/pi/GrovePi/Software/Python/grove_moisture.py'])
        else:
            print dweet
