import customtkinter as ctk

from frontend.widgets.sidebar import Sidebar
from frontend.widgets.camera_frame import CameraFrame

from .theme import *


class Dashboard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("AwakeSense")

        self.geometry("1450x850")

        self.configure(fg_color=BACKGROUND)

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        self.camera = CameraFrame(self)

        self.camera.grid(
            row=0,
            column=0,
            padx=25,
            pady=25,
            sticky="nsew"
        )

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=1,
            padx=(0, 25),
            pady=25,
            sticky="ns"
        )


if __name__ == "__main__":

    app = Dashboard()

    app.mainloop()