# Trezor (one), press my buttons.

A simple hardware testing drone for Trezor One.

![](demo.gif)

## Hardware

To build this simple bot, we are using:

* Arduino UNO R3 (or compatible)
* 2x Tower Pro Micro Servo 9g SG9

## Software

* ```arduino/``` includes the code for the hardware
* ```scripts/``` includes the control scripts

## 3D Models

* ```model/``` includes the STL as well as OpenSCAD files

## TODO

* Build python library around ``uhubctl``
* Build in a standalone application for testing scenarions
  * ``yaml`` as input
  * concurency for multiple trezors
* Add webcam support (model support)
  * ``mp4`` recordings as artifacts 
  * Recording of the CI test over the recording of the webcam with opacity
* Integrate the arduino board box into the model
* Figure out docker forwaring of device files for GitLab CI
* Add Trezor T support
