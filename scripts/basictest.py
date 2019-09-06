#!/usr/bin/env -S python3 -u
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
    print("[software]  Waiting for {} seconds...".format(seconds));
    time.sleep(seconds);

def now():
    print("\n[timestamp] {}".format(datetime.datetime.now()));

def basic_test(ser):
    trezor_poweroff();
    trezor_poweron();
    wait(2)
    touch(ser, "right", "click");
    wait(3);
    touch(ser, "right", "click");
    wait(3)
    print("[software/trezorctl] ping -b TPMBping");
    os.system("trezorctl ping -b TPMBping &");
    wait(5);
    touch(ser, "right", "click");
    wait(5)
    print("[software/trezorctl] wipe-device");
    os.system("trezorctl wipe-device &");
    wait(5);
    touch(ser, "right", "click");
    wait(5);
    print("[software/trezorctl] reset-device");
    os.system("trezorctl reset-device -l tpmb -s &");
    wait(5);
    touch(ser, "right", "click");
    wait(5);
    print("[software/trezorctl] get_address --coin Bitcoin --script-type address --address \"m/44'/0'/0'/0/0\" -d");
    os.system("trezorctl get_address --coin Bitcoin --script-type address --address \"m/44'/0'/0'/0/0\" -d &");
    wait(5);
    touch(ser, "right", "click");
    wait(2);
    print("Basic test is done.");



def main():
    ser = serial.Serial(arduino_serial, 9600)
    basic_test(ser);

if __name__ == "__main__":
    main()

