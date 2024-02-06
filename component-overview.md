# Hop by Team Hooper. 
Hop is an automated waste management system designed to help healthcare workers smoothen the sorting of composite and single material waste for recycling. Refer to our Github link for the source code. For the Arduino sketch was uploaded to an ESP32S3 DevKitC board. Refer to documentation below for the respective code and function of individual components of Hop.

## Components
# Roller
For our proof-of-concept, the current mechanism consists of 2 TT gear motors which are controlled by a L293D H-bridge driver and ESP32S3 DevKitC board. The 2 motors spin in opposite directions. Each motor was attached to 1 Styrofoam cone via a couple made out of wood. Each Styrfoam cone was covered in tape to increase the friction coefficient of the area that contacts the waste. Currently, the code starts the roller once the board is powered and the motors run continuously. Moving forward, there are plans to add in a functionality that turns on the roller mechanism only when a material is placed in the roller (using sensors).

# Hopper
For our proof-of-concept, the current mechanism consists of 2 SG90 Micro Servo motors which are controlled by a ESP32S3 DevKitC board. Each servo motor is attached to a panel cut from cardboard via a plastic coupler. The Arduino sketch contains 2 functions, servoDrop() and servo1Drop(), that each causes their respective panel to open and dispense an item into the respective bins. For the demo, our code continuously calls each function to open each panel in an alternating fashion.

# ESP32-CAM
The ESP32-CAM module is a crucial component of Hop, providing the visual input required for identifying different types of waste. It captures images of the waste items as they are presented to the system. The compact and powerful ESP32-CAM module is chosen for its affordability and ease of integration with the ESP32S3 DevKitC board, offering WiFi connectivity that enables real-time image processing and classification capabilities.

# Object Recognition with Computer Vision Model
For object recognition, Hop will utilise the YOLOv8 model along with OpenCV to analyse the images captured by the ESP32-CAM. YOLOv8, being one of the latest iterations of  the open-sourced computer vision AI models, offers exceptional speed and accuracy in detecting objects within images. This model is trained to differentiate between composite and single-material waste items, enabling Hop to make informed decisions about sorting. OpenCV, a robust library for computer vision tasks, is used to preprocess the images for the YOLO model and to manage the interaction between the captured images and the model's inference engine.


## Future Development: Integration for Automated Sorting

In the next phase of development, Team Hooper plans to fully integrate the object recognition capabilities with the physical sorting mechanism. The process will work as follows:

1. **Material Detection**: As waste items are introduced into the system, the ESP32-CAM captures their images and sends them for processing. The YOLOv8 model, supported by OpenCV, analyses these images to identify and classify the waste materials.

2. **Signal Processing**: Once an item is recognised, the system categorises it as either composite or single-material waste. This classification is then communicated to the ESP32S3 DevKitC board via a predefined signal protocol.

3. **Automated Sorting**: Based on the signal received, the ESP32S3 board activates the appropriate servo motor (either `servoDrop()` or `servo1Drop()` function is called) to open the corresponding panel of the hopper. This action ensures that the item is dispensed into the correct bin designated for its material type.

4. **Continuous Improvement**: Team Hooper aims to refine the object recognition accuracy and sorting efficiency through iterative development and training of the YOLOv8 model with a broader dataset of waste materials. This ongoing improvement will enhance Hop's capability to handle a wider variety of waste items effectively.

## Conclusion
The integration of the ESP32-CAM with YOLOv8 and OpenCV for object recognition represents a significant advancement in Hop's development. This feature will enable automated, intelligent sorting of waste materials, furthering the project's goal of improving waste management processes within healthcare facilities. Team Hooper is committed to continuous innovation and integration, aiming to create a fully autonomous waste management system that is reliable, efficient, and scalable.