import math
import time


class BlinkDetector:

    def __init__(self):
        self.threshold = 0.23
        self.counter = 0
        self.closed = False
        self.closed_start = None
        self.closed_time = 0.0

        self.left_eye = [33, 160, 158, 133, 153, 144]
        self.right_eye = [362, 385, 387, 263, 373, 380]

    def distance(self, p1, p2):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    def calculate_ear(self, landmarks, eye):

        p1 = landmarks[eye[0]]
        p2 = landmarks[eye[1]]
        p3 = landmarks[eye[2]]
        p4 = landmarks[eye[3]]
        p5 = landmarks[eye[4]]
        p6 = landmarks[eye[5]]

        vertical = self.distance(p2, p6) + self.distance(p3, p5)
        horizontal = self.distance(p1, p4)

        return vertical / (2 * horizontal)

    def detect(self, landmarks):

        left = self.calculate_ear(landmarks, self.left_eye)
        right = self.calculate_ear(landmarks, self.right_eye)

        ear = (left + right) / 2

        if ear < self.threshold:

            if not self.closed:
                self.counter += 1
                self.closed = True
                self.closed_start = time.time()

            self.closed_time = time.time() - self.closed_start

        else:

            self.closed = False
            self.closed_time = 0.0
            self.closed_start = None

        return self.closed, ear, self.counter, self.closed_time