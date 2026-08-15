import cv2

from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService
from ai.face_mesh.face_mesh import FaceMeshDetector
from ai.blink_detection.blink_detector import BlinkDetector


def main():

    config = CameraConfig()

    camera = CameraService(config)

    mesh = FaceMeshDetector()

    blink = BlinkDetector()

    while True:

        frame = camera.read_frame()

        if frame is None:
            break

        results = mesh.detect(frame)

        if results.multi_face_landmarks:

            landmarks = results.multi_face_landmarks[0].landmark

            blinking, ear = blink.detect(landmarks)

            status = "BLINKING" if blinking else "OPEN"

            cv2.putText(
                frame,
                f"Eyes: {status}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"EAR: {ear:.3f}",
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