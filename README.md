# RealSense Video Capture

This repository contains a Python script that uses the Intel RealSense camera to capture video with color and depth information. The captured video is saved to a file while displaying the frames in real-time using OpenCV.

## Dependencies

- Python 3
- pyrealsense2
- OpenCV
- NumPy

## Installation

1. Clone this repository:

```git clone https://github.com/aniervs/depth-streaming-realsense.git```
 
2. Install the required dependencies using pip:

``pip install pyrealsense2 opencv-python numpy``
 
3. Connect the Intel RealSense camera to your computer.

## Usage

1. Navigate to the project directory:
```cd realsense-video-capture```
2. Run the script:
```python main.py``` 
3. The script will start capturing video from the RealSense camera. Press 'q' to stop the capture.

4. The captured video will be saved as 'output.mp4' in the project directory.


## Acknowledgements

- [Intel RealSense SDK](https://github.com/IntelRealSense/librealsense)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)


