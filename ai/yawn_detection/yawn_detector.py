import math


class YawnDetector:

    def __init__(self):
        self.threshold = 0.60
        self.counter = 0
        self.open = False

    def distance(self, p1, p2):
        return math.hypot(p1.x - p2.x, p1.y - p2.y)

    def detect(self, landmarks):

        upper = landmarks[13]
        lower = landmarks[14]

        left = landmarks[78]
        right = landmarks[308]

        vertical = self.distance(upper, lower)
        horizontal = self.distance(left, right)

        mar = vertical / horizontal

        if mar > self.threshold:
            if not self.open:
                self.counter += 1
                self.open = True
        else:
            self.open = False

        return self.open, mar, self.counter