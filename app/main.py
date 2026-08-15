import cv2

from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService
from ai.face_detection.face_detector import FaceDetector
from ai.face_mesh.face_mesh import FaceMeshDetector
from ai.blink_detection.blink_detector import BlinkDetector
from ai.yawn_detection.yawn_detector import YawnDetector
from ai.head_pose.head_pose import HeadPoseEstimator
from ai.fatigue_engine.fatigue_engine import FatigueEngine
from ai.session_logger.logger import SessionLogger
from ai.object_detection.object_detector import ObjectDetector

def main():

    config = CameraConfig()

    camera = CameraService(config)

    face_detector = FaceDetector()
    face_mesh = FaceMeshDetector()

    blink_detector = BlinkDetector()
    yawn_detector = YawnDetector()
    head_pose = HeadPoseEstimator()
    fatigue_engine = FatigueEngine()
    logger = SessionLogger()
    object_detector = ObjectDetector()

    while True:

        frame = camera.read_frame()
        phone_detected, detected_objects = object_detector.detect(frame)

        if frame is None:
            break

        face_results = face_detector.detect(frame)
        mesh_results = face_mesh.detect(frame)

        if face_results.detections:

            h, w, _ = frame.shape

            for detection in face_results.detections:

                box = detection.location_data.relative_bounding_box

                x = int(box.xmin * w)
                y = int(box.ymin * h)
                bw = int(box.width * w)
                bh = int(box.height * h)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + bw, y + bh),
                    (0, 255, 0),
                    2,
                )

        if mesh_results.multi_face_landmarks:

            landmarks = mesh_results.multi_face_landmarks[0].landmark

            blinking, ear, blink_count, closed_time = blink_detector.detect(landmarks)

            yawning, mar, yawn_count = yawn_detector.detect(landmarks)
            head_direction, angle = head_pose.detect(landmarks)
            fatigue, status = fatigue_engine.detect(
                blink_count,
                yawn_count,
                closed_time
            )

            logger.save(
                blink_count,
                yawn_count,
                fatigue,
                status
            )

            cv2.putText(
                frame,
                "AwakeSense AI",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Eyes : {'CLOSED' if blinking else 'OPEN'}",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Blinks : {blink_count}",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"EAR : {ear:.3f}",
                (20, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Mouth : {'YAWNING' if yawning else 'NORMAL'}",
                (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Yawns : {yawn_count}",
                (20, 190),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"MAR : {mar:.3f}",
                (20, 220),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Head : {head_direction}",
                (20, 250),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

            cv2.putText(
                frame,
                f"Fatigue : {fatigue}%",
                (20, 280),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2,
            )

            cv2.putText(
                frame,
                f"Status : {status}",
                (20, 310),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2,
            )

            cv2.putText(
                frame,
                f"Phone : {'YES' if phone_detected else 'NO'}",
                (20, 340),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255) if phone_detected else (0, 255, 0),
                2,
            )
        cv2.rectangle(frame, (10, 10), (360, 380), (40, 40, 40), -1)
        cv2.rectangle(frame, (10, 10), (360, 380), (0, 255, 255), 2)
        cv2.imshow("AwakeSense", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()


if __name__ == "__main__":
    main()