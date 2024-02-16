import cv2
import subprocess
import numpy as np
from roboflow import Roboflow

# Load Roboflow model
rf = Roboflow(api_key="rz0A8V6lWKzJHGDrFe89")
project = rf.workspace("healthhack").project("hop-tiny")
version = project.version("3")
model = version.model

print("Model loaded successfully!")

# Define the command to start the libcamera-vid process.
# Here, we're outputting the video in a raw format that OpenCV can read.
# Adjust the capture resolution and other parameters as needed.
libcamera_vid_cmd = [
    'libcamera-vid',
    '-n',  # No preview window.
    '--codec', 'yuv420',  # Output format compatible with OpenCV.
    '-t', '0',  # Run indefinitely until stopped.
    '--width', '640',  # Video width.
    '--height', '480',  # Video height.
    '-o', '-'  # Output to stdout.
]

# Start the libcamera-vid process.
process = subprocess.Popen(libcamera_vid_cmd, stdout=subprocess.PIPE, bufsize=10**8)

# Calculate the size of each frame.
# For YUV420, the size is 1.5 times the width times the height because
# the U and V (chroma) components are subsampled by a factor of 2.
frame_size = int(640 * 480 * 1.5)

try:
    while True:
        # Read a single frame from stdout of the libcamera-vid process.
        frame_data = process.stdout.read(frame_size)

        if len(frame_data) != frame_size:
            print("Failed to read complete frame. Exiting")
            break

        # Convert the raw frame data to a NumPy array.
        # First, reshape the data into the YUV420 format.
        yuv420p_frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((int(480 * 1.5), 640))

        # Convert YUV420 to BGR for OpenCV processing.
        bgr_frame = cv2.cvtColor(yuv420p_frame, cv2.COLOR_YUV2BGR_I420)
        
        # Config inference setting
        model.confidence = 20
        model.overlap = 25

        # Perform inference
        predictions = model.predict(bgr_frame)
        
        print(predictions.json())
        
        # Visualize predictions
        for prediction in predictions:
            x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
            x1, y1 = int(x), int(y)
            x2, y2 = int(x + width), int(y + height)
            # Concatenate class label with confidence level rounded to two decimal points
            label = f"{prediction['class']} ({round(prediction['confidence'], 2)})"
            cv2.rectangle(bgr_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(bgr_frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Display the frame.
        cv2.imshow('Frame', bgr_frame)

        # Break the loop by pressing 'q'.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Ensure the subprocess and OpenCV window are cleaned up properly.
    process.kill()
    cv2.destroyAllWindows()

