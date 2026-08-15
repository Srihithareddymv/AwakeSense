import customtkinter as ctk


class CameraFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            corner_radius=25
        )