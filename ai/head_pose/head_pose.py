from .pose_utils import calculate_angle


class HeadPoseEstimator:

    def __init__(self):
        self.left_face = 234
        self.right_face = 454
        self.nose = 1

    def detect(self, landmarks):

        left = landmarks[self.left_face]
        right = landmarks[self.right_face]
        nose = landmarks[self.nose]

        angle = calculate_angle(left, right)

        center = (left.x + right.x) / 2

        if nose.x < center - 0.03:
            direction = "LEFT"

        elif nose.x > center + 0.03:
            direction = "RIGHT"

        else:
            direction = "FORWARD"

        return direction, angle