from frontend.views.ai_controller import AIController
from frontend.views.detection_pipeline import DetectionPipeline


class AppController:

    def __init__(self):

        self.ai = AIController()

        self.pipeline = DetectionPipeline(
            self.ai
        )