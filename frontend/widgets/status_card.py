import customtkinter as ctk


class StatusCard(ctk.CTkFrame):

    def __init__(self, master, title):

        super().__init__(
            master,
            corner_radius=18,
            height=60
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text=title,
            font=("Poppins", 18, "bold")
        ).pack(pady=15)