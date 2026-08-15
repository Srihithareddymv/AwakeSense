import customtkinter as ctk


class CameraWidget(ctk.CTkLabel):

    def __init__(self, master):

        super().__init__(
            master,
            text="📷\n\nCamera Loading...",
            font=("Poppins", 28),
            corner_radius=25
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )