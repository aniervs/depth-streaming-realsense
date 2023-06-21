import json
import pyrealsense2 as rs


def get_settings():
    with open("settings.json", 'r') as json_file:
        settings = json.load(json_file)
    return settings


def apply_settings(frame, settings):
    if "Decimation Filter" in settings and settings["Decimation Filter"]["enabled"]:
        decimation = rs.decimation_filter()
        decimation.set_option(rs.option.filter_magnitude, settings["Decimation Filter"]["filter_magnitude"])
        frame = decimation.process(frame)

    if "Threshold Filter" in settings and settings["Threshold Filter"]["enabled"]:
        threshold = rs.threshold_filter()
        threshold.set_option(rs.option.min_distance, settings["Threshold Filter"]["min_distance"])
        threshold.set_option(rs.option.max_distance, settings["Threshold Filter"]["max_distance"])
        frame = threshold.process(frame)

    if "Spatial Filter" in settings and settings["Spatial Filter"]["enabled"]:
        spatial = rs.spatial_filter()
        spatial.set_option(rs.option.filter_magnitude, settings["Spatial Filter"]["filter_magnitude"])
        spatial.set_option(rs.option.filter_smooth_alpha, settings["Spatial Filter"]["filter_smooth_alpha"])
        spatial.set_option(rs.option.filter_smooth_delta, settings["Spatial Filter"]["filter_smooth_delta"])
        frame = spatial.process(frame)

    if "Temporal Filter" in settings and settings["Temporal Filter"]["enabled"]:
        temporal = rs.temporal_filter()
        temporal.set_option(rs.option.filter_smooth_alpha, settings["Temporal Filter"]["filter_smooth_alpha"])
        temporal.set_option(rs.option.filter_smooth_delta, settings["Temporal Filter"]["filter_smooth_delta"])
        frame = temporal.process(frame)

    return frame
