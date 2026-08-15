import cv2

from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService
from ai.face_mesh.face_mesh import FaceMeshDetector
from ai.yawn_detection.yawn_detector import YawnDetector


def main():

    config = CameraConfig()
    camera = CameraService(config)
    mesh = FaceMeshDetector()
    yawn = YawnDetector()

    while True:

        frame = camera.read_frame()

        if frame is None:
            break

        results = mesh.detect(frame)

        if results.multi_face_landmarks:

            landmarks = results.multi_face_landmarks[0].landmark

            yawning, mar = yawn.detect(landmarks)

            status = "YAWNING" if yawning else "NORMAL"

            cv2.putText(
                frame,
                f"Mouth: {status}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"MAR: {mar:.3f}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow(config.window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()


if __name__ == "__main__":
    main()