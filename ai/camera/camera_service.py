import cv2
from .camera_config import CameraConfig


class CameraService:
    def __init__(self, config: CameraConfig):
        self.config = config

        self.camera = cv2.VideoCapture(config.camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to access webcam.")

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, config.width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, config.height)
        self.camera.set(cv2.CAP_PROP_FPS, config.fps)

    def read_frame(self):
        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def release(self):
        self.camera.release()
        cv2.destroyAllWindows()