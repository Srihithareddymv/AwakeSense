from .fatigue_score import FatigueScore


class FatigueEngine:

    def __init__(self):
        self.score = FatigueScore()

    def detect(
        self,
        blink_count,
        yawn_count,
        closed_time
    ):

        fatigue = self.score.calculate(
            blink_count,
            yawn_count,
            closed_time
        )

        # Emergency condition (matches your alarm)
        if closed_time >= 7:
            status = "DROWSINESS DETECTED"

        elif fatigue < 30:
            status = "ALERT"

        elif fatigue < 60:
            status = "TIRED"

        else:
            status = "DROWSY"

        return fatigue, status