from frontend.views.main_window import MainWindow

from frontend.views.ai_controller import AIController

from frontend.views.dashboard_controller import DashboardController


class Application:

    def __init__(self):

        self.window = MainWindow()

        self.ai = AIController()

        self.dashboard = DashboardController(
            self.window
        )

    def run(self):

        self.window.mainloop()