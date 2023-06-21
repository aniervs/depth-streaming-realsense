import pyrealsense2 as rs
import cv2
import numpy as np
from utils import get_settings, apply_settings

settings = get_settings()

filename = input('Enter output file name: ')
rgb_video = "data/" + filename + ".mp4"
depth_video = "data/" + filename + "_depth.mp4"

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

pipeline.start(config)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30
video_writer_rgb = None
video_writer_depth = None

try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        depth_frame = apply_settings(depth_frame, settings["Depth"])

        if not color_frame or not depth_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        depth_image = cv2.resize(depth_image, (color_image.shape[1], color_image.shape[0]))

        if video_writer_rgb is None or video_writer_depth is None:
            height_rgb, width_rgb = color_image.shape[:2]
            height_depth, width_depth = depth_image.shape[:2]

            video_writer_rgb = cv2.VideoWriter(rgb_video, fourcc, fps, (width_rgb, height_rgb))
            video_writer_depth = cv2.VideoWriter(depth_video, fourcc, fps, (width_depth, height_depth))

        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.25), cv2.COLORMAP_RAINBOW)

        video_writer_depth.write(depth_colormap)
        video_writer_rgb.write(color_image)

        cv2.imshow('RealSense Capture', color_image)
        cv2.imshow('RealSense Depth', depth_colormap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()

    if video_writer_rgb is not None and video_writer_depth:
        video_writer_rgb.release()
        video_writer_depth.release()

    cv2.destroyAllWindows()

