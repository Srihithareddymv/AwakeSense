from frontend.views.dashboard_updater import DashboardUpdater


class DashboardController:

    def __init__(self, window):

        self.dashboard = DashboardUpdater(window)