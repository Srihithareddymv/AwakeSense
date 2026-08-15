import cv2
from PIL import Image, ImageTk


class LiveCamera:

    def __init__(self, window, label, processor, dashboard):

        self.window = window
        self.label = label
        self.processor = processor
        self.dashboard = dashboard

        self.update()

    def update(self):

        result = self.processor.get_frame()

        if result is not None:

            frame = result["frame"]

            frame = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )

            image = Image.fromarray(frame)

            image = image.resize(
                (900, 700)
            )

            photo = ImageTk.PhotoImage(image)

            self.label.configure(
                image=photo,
                text=""
            )

            self.label.image = photo

            self.dashboard.update(
                result["eyes"],
                result["blinks"],
                result["yawns"],
                result["head"],
                result["phone"],
                result["fatigue"],
                result["status"]
            )

            # =========================
            # EMERGENCY MODE
            # =========================

            if result["status"] == "DROWSINESS DETECTED":

                self.window.show_emergency()

            else:

                self.window.hide_emergency()

        self.label.after(
            15,
            self.update
        )