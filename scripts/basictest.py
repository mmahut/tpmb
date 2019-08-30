#!/usr/bin/env python3
# This is just a dirty playground, do not use.
# It will be refactored over time.

import os
import sys
import serial
import time

uhub_loction = "1-9";
uhub_port = "1";

def trezor_poweroff():
    print("*** Turning power off...");
    os.system(("uhubctl -l {} -p {} -r 100 -a off > /dev/null").format(uhub_loction, uhub_port));
    wait(3)

def trezor_poweron():
    print("*** Turning power on...");
    os.system(("uhubctl -l {} -p {} -a on > /dev/null").format(uhub_loction, uhub_port));
    wait(3)

def touch(ser, location, action):
    print("*** Touching the {} button by {}...".format(location, action));
    ser.write(("{} {}\n".format(location, action)).encode())

def wait(seconds):
    print("*** Waiting for {} seconds...".format(seconds));
    time.sleep(seconds);

def basic_test(ser):
    trezor_poweroff();
    trezor_poweron();
    os.system("trezorctl ping -b TPMBping &");
    wait(2);
    touch(ser, "right", "click");
    wait(5)
    os.system("trezorctl wipe-device &");
    wait(2);
    touch(ser, "right", "click");
    wait(5);
    os.system("trezorctl reset-device -l tpmb -s &");
    wait(2);
    touch(ser, "right", "click");
    wait(5);
    os.system("trezorctl get_address --coin Bitcoin --script-type address --address \"m/44'/0'/0'/0/0\" -d &");
    wait(2);
    touch(ser, "right", "click");
    wait(2);



def main():
    ser = serial.Serial("/dev/ttyACM1", 9600)
    basic_test(ser);

if __name__ == "__main__":
    main()

