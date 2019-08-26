#!/usr/bin/env python3
import os
import serial
import time
ser = serial.Serial("/dev/ttyACM1", 9600)

print("Turnining off usb power.")
os.system("uhubctl -a off -l 1-10 -p 2")

print("Pressing right buttong")
ser.write("pess right".encode())

print("Turning on usb power")
os.system("uhubctl -a on -l 1-10 -p 2")
time.sleep(5);

print("Unpressing the right button.")
ser.write("unpress right".encode())

print("Updating the firmware.")
updatefw = "trezorctl firmware-update -u https://firmware.corp.sldev.cz/legacy/firmwares/tsusanka/ci-deploy/2019-08-16-legacy-firmware-4381fe01"
os.system(updatefw);
