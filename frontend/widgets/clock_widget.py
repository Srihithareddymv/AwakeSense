import customtkinter as ctk
from datetime import datetime


class ClockWidget(ctk.CTkLabel):

    def __init__(self, master):

        super().__init__(
            master,
            font=("Poppins", 16),
            text_color="#666666"
        )

        self.update_time()

    def update_time(self):

        self.configure(
            text=datetime.now().strftime("%A\n%d %b %Y\n%I:%M:%S %p")
        )

        self.after(
            1000,
            self.update_time
        )