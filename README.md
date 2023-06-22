# RealSense Video Capture

This repository contains code that uses the Intel RealSense camera to capture video with color and depth information. The captured videos are saved to a file while displaying the frames in real-time using OpenCV.

## Installation

1. Clone this repository and navigate to the project folder:

```Bash
git clone https://github.com/aniervs/depth-streaming-realsense.git && cd depth-streaming-realsense
```
2. Create a virtual environment and install the dependencies:

```Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
 
3. Connect the Intel RealSense camera to your computer.

## Usage

1. Set the preprocessing settings you want for the recordings on the 'settings.json' file.
2. Run the 'main.py' file to start recording.
3. The script will start capturing video from the RealSense camera. Press 'q' to stop the capture.
4. The recordings will be stored under the 'data' folder, where you'll have two videos: one with the color image and another with the depth image.

## Supported post-processing filters 
  - [x] Decimation filter
  - [ ] HDR Merge
  - [ ] Filter by Sequence id
  - [x] Threshold Filter
  - [ ] Depth to Disparity
  - [x] Spatial Filter
  - [x] Temporal Filter
  - [ ] Hole Filling Filter
  - [ ] Disparity to Depth
