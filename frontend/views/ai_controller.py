from ai.alerts.alarm import Alarm
from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService

from ai.face_detection.face_detector import FaceDetector
from ai.face_mesh.face_mesh import FaceMeshDetector

from ai.blink_detection.blink_detector import BlinkDetector
from ai.yawn_detection.yawn_detector import YawnDetector

from ai.head_pose.head_pose import HeadPoseEstimator
from ai.fatigue_engine.fatigue_engine import FatigueEngine
from ai.object_detection.object_detector import ObjectDetector


class AIController:

    def __init__(self):

        self.camera = CameraService(CameraConfig())

        self.face_detector = FaceDetector()
        self.face_mesh = FaceMeshDetector()

        self.blink_detector = BlinkDetector()
        self.yawn_detector = YawnDetector()

        self.head_pose = HeadPoseEstimator()

        self.fatigue_engine = FatigueEngine()

        self.alarm = Alarm()

        self.object_detector = ObjectDetector()