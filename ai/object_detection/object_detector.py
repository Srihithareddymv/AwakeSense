from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):

        self.model = YOLO("yolov8n.pt")

        self.phone_classes = [
            "cell phone"
        ]

    def detect(self, frame):

        results = self.model(frame, verbose=False)

        detected = False

        objects = []

        for result in results:

            for box in result.boxes:

                cls = int(box.cls)

                label = self.model.names[cls]

                if label in self.phone_classes:

                    detected = True

                    objects.append({
                        "label": label,
                        "box": box.xyxy[0].tolist(),
                        "confidence": float(box.conf)
                    })

        return detected, objects