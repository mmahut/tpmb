#!/usr/bin/env python3

# This is just a dirty playground, do not use.
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

def update_firmware(ser, version):
    if "http" in version:
        unofficial = True;
        trezorctlcmd = "trezorctl firmware-update -s -u {} >/dev/null &".format(version);
    else:
        unofficial = False;
        trezorctlcmd = "trezorctl firmware-update -v {} >/dev/null &".format(version);
    trezor_poweroff();
    touch(ser, "left", "press");
    trezor_poweron();
    touch(ser, "left", "unpress");
    print("*** Updating the fireware to {}...".format(version));
    os.system(trezorctlcmd);
    wait(3);
    touch(ser, "right", "click");
    wait(30);
    if unofficial: touch(ser, "right", "click");
    wait(5);
    trezor_poweroff();
    trezor_poweron();
    if unofficial: touch(ser, "right", "click");
    if unofficial: wait(5);
    if unofficial: touch(ser, "right", "click");
    wait(5);
    os.system("trezorctl get-features");

def main():
    ser = serial.Serial("/dev/ttyACM1", 9600)
    update_firmware(ser, sys.argv[1]);

if __name__ == "__main__":
    main()

