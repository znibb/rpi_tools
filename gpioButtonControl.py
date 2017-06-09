#!/usr/bin/env python

import signal
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

button1_pin = 10
button2_pin = 26
debounceTime = 500

GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def signal_handler(signum, frame):
        GPIO.cleanup()

def button1_callback(channel):
        os.system("sudo shutdown -h")

def button2_callback(channel):
        os.system("sudo python /home/znibb/scripts/pushbullet_network_info.py")


if __name__ == "__main__":
        # Setup signal handler to exit gracefully
        signal.signal(signal.SIGTERM, signal_handler)

        # Enable interrupts
        GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button1_callback, bouncetime=debounceTime)
        GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=button2_callback, bouncetime=debounceTime)

        # Main loop
        while(True):
                pass

