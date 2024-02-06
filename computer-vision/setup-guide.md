
## Setup Instructions

### Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- OpenCV
- Matplotlib
- Ultralytics YOLO library

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/evanyan13/hooper.git
cd hooper
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

This command will install all necessary Python libraries, including OpenCV, Matplotlib, and the Ultralytics YOLO package.

### Model Setup

1. **Download Pre-trained Models:**

   Make sure to download the necessary pre-trained model files and place them in the `src` directory. These files include:

   - `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
   - `frozen_inference_graph.pb`

2. **Label Files:**

   Ensure the `labels.txt` file, containing class labels for detected objects, is placed in the `src` directory.

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

## License

Specify your project's license here.

## Contact

For any questions or feedback regarding the Hop project, please contact Team Hooper at [contact information].