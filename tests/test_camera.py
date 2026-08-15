import cv2

from ai.camera.camera_config import CameraConfig
from ai.camera.camera_service import CameraService
from ai.face_detection.face_detector import FaceDetector


def main():
    config = CameraConfig()

    camera = CameraService(config)

    detector = FaceDetector()

    while True:

        frame = camera.read_frame()

        if frame is None:
            break

        results = detector.detect(frame)

        if results.detections:

            height, width, _ = frame.shape

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                x = int(bbox.xmin * width)
                y = int(bbox.ymin * height)
                w = int(bbox.width * width)
                h = int(bbox.height * height)

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

        cv2.imshow(config.window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()


if __name__ == "__main__":
    main()