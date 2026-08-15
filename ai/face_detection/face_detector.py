import cv2
import mediapipe as mp


class FaceDetector:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection

        self.detector = self.mp_face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=0.6
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.detector.process(rgb)

        return results