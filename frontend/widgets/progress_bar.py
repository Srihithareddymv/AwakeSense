import customtkinter as ctk


class FatigueBar(ctk.CTkProgressBar):

    def __init__(self, master):

        super().__init__(
            master,
            width=220,
            height=18,
            corner_radius=20
        )

        self.set(0)