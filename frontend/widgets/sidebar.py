import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=320,
            corner_radius=25
        )

        self.pack_propagate(False)