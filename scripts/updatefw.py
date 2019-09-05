#!/usr/bin/env python3
# This is just a dirty playground, do not use.
# It will be refactored over time.

import os
import sys
import serial
import time
import yaml
import datetime

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

uhub_loction = cfg['usb_location'];
uhub_port = cfg['usb_port'];
arduino_serial = cfg['arduino_serial'];

def trezor_poweroff():
    now();
    print("[hardware/usb] Turning power off...");
    os.system(("uhubctl -l {} -p {} -r 100 -a off > /dev/null").format(uhub_loction, uhub_port));
    wait(3)

def trezor_poweron():
    now();
    print("[hardware/usb] Turning power on...");
    os.system(("uhubctl -l {} -p {} -a on > /dev/null").format(uhub_loction, uhub_port));
    wait(3)

def touch(ser, location, action):
    now();
    print("[hardware/trezor] Touching the {} button by {}...".format(location, action));
    ser.write(("{} {}\n".format(location, action)).encode())

def wait(seconds):
    now();
    print("[software] Waiting for {} seconds...".format(seconds));
    time.sleep(seconds);

def now():
    print("\n[timestamp] {}".format(datetime.datetime.now()));

def update_firmware(ser, version):
    if "http" in version:
        unofficial = True;
        trezorctlcmd = "trezorctl firmware-update -s -u {} &".format(version);
    else:
        unofficial = False;
        trezorctlcmd = "trezorctl firmware-update -v {} &".format(version);
    trezor_poweroff();
    if "1.8" in version:
        touch(ser, "left", "press");
    else:
        touch(ser, "all", "press");
    wait(2);
    trezor_poweron();
    wait(2);
    touch(ser, "all", "unpress");
    print("[software/trezorctl] Updating the firmware to {}...".format(version));
    os.system(trezorctlcmd);
    wait(3);
    touch(ser, "right", "click");
    wait(20);
    if unofficial: touch(ser, "right", "click");
    wait(5);
    trezor_poweroff();
    trezor_poweron();
    if unofficial: touch(ser, "right", "click");
    if unofficial: wait(5);
    if unofficial: touch(ser, "right", "click");
    wait(5);
    os.system("trezorctl get-features|grep version");

def main():
    ser = serial.Serial(arduino_serial, 9600)
    update_firmware(ser, sys.argv[1]);

if __name__ == "__main__":
    main()

