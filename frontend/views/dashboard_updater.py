class DashboardUpdater:

    def __init__(self, window):

        self.window = window

    def update(
        self,
        eyes,
        blinks,
        yawns,
        head,
        phone,
        fatigue,
        status
    ):

        self.window.labels["👀 Eyes"].configure(
            text=f"👀 Eyes : {eyes}"
        )

        self.window.labels["😉 Blinks"].configure(
            text=f"😉 Blinks : {blinks}"
        )

        self.window.labels["🥱 Yawns"].configure(
            text=f"🥱 Yawns : {yawns}"
        )

        self.window.labels["🧠 Head"].configure(
            text=f"🧠 Head : {head}"
        )

        self.window.labels["📱 Phone"].configure(
            text=f"📱 Phone : {'YES' if phone else 'NO'}"
        )

        self.window.labels["😴 Fatigue"].configure(
            text=f"😴 Fatigue : {fatigue}%"
        )

        self.window.labels["💗 Status"].configure(
            text=f"💗 Status : {status}"
        )

        self.window.progress.set(fatigue / 100)