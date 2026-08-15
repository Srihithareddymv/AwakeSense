class FatigueScore:

    def calculate(self, blinks, yawns, closed_time):

        score = 0

        score += blinks * 2
        score += yawns * 10
        score += int(closed_time * 25)

        return min(score, 100)