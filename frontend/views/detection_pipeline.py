class DetectionPipeline:

    def __init__(self, ai):

        self.ai = ai

    def process(self):

        frame = self.ai.camera.read_frame()

        if frame is None:
            return None

        # =========================
        # FACE DETECTION
        # =========================

        face_results = self.ai.face_detector.detect(frame)

        mesh_results = self.ai.face_mesh.detect(frame)

        if not mesh_results.multi_face_landmarks:

            self.ai.alarm.stop()

            return {
                "frame": frame,
                "eyes": "NO FACE",
                "blinks": 0,
                "yawns": 0,
                "head": "UNKNOWN",
                "phone": False,
                "fatigue": 0,
                "status": "NO FACE"
            }

        landmarks = mesh_results.multi_face_landmarks[0].landmark

        # =========================
        # BLINK DETECTION
        # =========================

        blinking, ear, blink_count, closed_time = \
            self.ai.blink_detector.detect(landmarks)

        # =========================
        # YAWN DETECTION
        # =========================

        yawning, mar, yawn_count = \
            self.ai.yawn_detector.detect(landmarks)

        # =========================
        # HEAD POSE
        # =========================

        head, angle = \
            self.ai.head_pose.detect(landmarks)

        # =========================
        # FATIGUE
        # =========================

        fatigue, status = \
            self.ai.fatigue_engine.detect(
                blink_count,
                yawn_count,
                closed_time
            )

        # =========================
        # PHONE DETECTION
        # =========================

        phone, objects = \
            self.ai.object_detector.detect(frame)

        # =========================
        # ALARM
        # =========================

        # Alarm if eyes are closed for 7+ seconds
        # OR a phone is detected

        if closed_time >= 7 or phone:

            self.ai.alarm.play()

        else:

            self.ai.alarm.stop()

        # =========================
        # RETURN RESULTS
        # =========================

        return {
            "frame": frame,
            "eyes": "CLOSED" if blinking else "OPEN",
            "blinks": blink_count,
            "yawns": yawn_count,
            "head": head,
            "phone": phone,
            "fatigue": fatigue,
            "status": status
        }