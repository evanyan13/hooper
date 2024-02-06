# Setup Guide for ESP32-CAM and Servo Motor Control

This guide provides detailed steps for setting up and running the ESP32-CAM module for capturing images and controlling servo motors using the ESP32S3 board. These components are part of the Hop project by Team Hooper, aimed at automating waste management.

## Prerequisites

Before starting, ensure you have the following:

- ESP32-CAM module
- ESP32S3 development board
- Two servo motors
- Suitable cables and connectors
- Arduino IDE installed on your computer

## Software Setup

### Arduino IDE Configuration

1. Install the Arduino IDE and open it.
2. Go to **File > Preferences** and add the ESP32 board manager URL to the Additional Board Manager URLs field: `https://dl.espressif.com/dl/package_esp32_index.json`
3. Open **Tools > Board > Boards Manager**, search for ESP32, and install the latest version.
4. Select your ESP32 board from **Tools > Board**.

### Code Upload

1. Open the provided ESP32-CAM code in Arduino IDE.
2. Select the correct port and board configuration under the Tools menu.
3. Upload the ESP32-CAM code to your ESP32-CAM module.
4. Repeat the process for the servo motor control code, but upload it to the ESP32S3 board.

## Running the Project

- After successfully uploading the codes, the ESP32-CAM module should start capturing images.
- The ESP32S3 board will control the servo motors to demonstrate waste sorting by moving the servos to predefined positions.


For further assistance or questions, please refer to the project's contact information.

