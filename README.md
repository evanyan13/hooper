# Hop - Automated Medical Waste Management System

Hop is an innovative automated waste management system designed by Team Hooper. It aims to assist healthcare workers in efficiently sorting composite and single-material waste for recycling. Utilizing advanced object recognition technology, Hop enhances the recycling processes within healthcare facilities, contributing to environmental sustainability.

## Project Overview

The Hop system leverages a custom object recognition model to differentiate between various types of waste, ensuring accurate sorting and disposal. This documentation outlines the setup process, usage, and technical details of the object recognition model implemented in this project.

## Setup Instructions

Please refer to the following installation guide within each category.
- Object Detection Model (Computer Vision): [Setup Guide](https://github.com/evanyan13/hooper/blob/main/cv/setup-guide.md)
- Hardware: [Setup Guide](https://github.com/evanyan13/hooper/blob/main/hardware/setup-guide.md)

## Usage

The project is structured to process images for object recognition, demonstrating capabilities with both static images and real-time webcam feed. 

- To process a static image and detect objects, run the script corresponding to image processing.
- For real-time object detection using a webcam, ensure you have a webcam connected and run the appropriate script.

## Documentation

### Object Recognition Model

The core of the Hop system is built on OpenCV's DNN module and Ultralytics' YOLO implementation. It includes the following key components:

- **Model Loading:** Utilizes OpenCV for loading SSD MobileNet and sets up YOLO for real-time detection.
- **Image Processing:** Demonstrates how to read and preprocess images for object detection.
- **Real-Time Detection:** Details the setup for using a webcam to capture video and perform object detection in real time.

### Scripts Overview

- **Image Detection:** Scripts related to loading models, processing images, and detecting objects within static images.
- **Webcam Detection:** Scripts for initializing a webcam, processing the video feed, and applying the object detection model in real time.

## Contributing

We welcome contributions to the Hop project! If you have suggestions or improvements, please fork the repository and submit a pull request.

## Contact

For any questions or feedback regarding the Hop project, please contact Team Hooper at evanyan@u.nus.edu.
