from dataclasses import dataclass


@dataclass
class CameraConfig:
    camera_index: int = 0
    width: int = 1280
    height: int = 720
    fps: int = 30
    window_name: str = "AwakeSense"