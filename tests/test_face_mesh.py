import cv2
import mediapipe as mp

from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService
from ai.face_mesh.face_mesh import FaceMeshDetector

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh


def main():

    config = CameraConfig()

    camera = CameraService(config)

    detector = FaceMeshDetector()

    while True:

        frame = camera.read_frame()

        if frame is None:
            break

        results = detector.detect(frame)

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                mp_drawing.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION
                )

        cv2.imshow(config.window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()


if __name__ == "__main__":
    main()