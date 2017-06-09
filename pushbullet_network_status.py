#!/usr/bin/env python

# Load API token
execfile("api_token_pushbullet.secret")

# Import libs
from pushbullet import Pushbullet
from urllib2 import urlopen

import socket
import fcntl
import struct
import os
import subprocess

# Function for retrieving local IP
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

# Create Pushbullet object
try:
	pb = Pushbullet(PUSHBULLET_API_TOKEN)
except NameError:
	print("Error: Missing Pushbullet token")
	quit()

# Get system information
local_ip_address = get_ip_address('wlan0')
global_ip_address = urlopen('http://ip.42.pl/raw').read()
ssid_raw = subprocess.check_output("iwgetid", shell=False)
ssid = ssid_raw[17:-2]
hostname_raw = subprocess.check_output("hostname", shell=False)
hostname = hostname_raw[:-1]

# Create message strings
header_string = "Status for: " + hostname

message_string = "SSID: " + ssid + \
		"\nLocal IP: " + local_ip_address + \
                "\nGlobal IP: " + global_ip_address

# Push notification
push = pb.push_note(header_string, message_string)

