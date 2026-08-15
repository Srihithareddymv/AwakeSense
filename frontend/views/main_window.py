import customtkinter as ctk

from frontend.dashboard.theme import *
from frontend.views.camera_widget import CameraWidget
from frontend.views.live_camera import LiveCamera
from frontend.views.frame_processor import FrameProcessor
from frontend.views.dashboard_updater import DashboardUpdater
from frontend.widgets.clock_widget import ClockWidget


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("AwakeSense")
        self.geometry("1650x980")
        self.minsize(1200, 750)

        self.configure(
            fg_color=BACKGROUND
        )

        # =========================
        # MAIN WINDOW GRID
        # =========================

        self.grid_columnconfigure(
            0,
            weight=5
        )

        self.grid_columnconfigure(
            1,
            weight=2
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        # =========================
        # CAMERA FRAME
        # =========================

        self.camera_frame = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=30,
            border_width=2,
            border_color=BORDER
        )

        self.camera_frame.grid(
            row=0,
            column=0,
            padx=(25, 10),
            pady=25,
            sticky="nsew"
        )

        self.camera_frame.grid_rowconfigure(
            0,
            weight=1
        )

        self.camera_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.camera = CameraWidget(
            self.camera_frame
        )

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=30,
            border_width=2,
            border_color=BORDER
        )

        self.sidebar.grid(
            row=0,
            column=1,
            padx=(10, 25),
            pady=25,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        # =========================
        # TITLE
        # =========================

        title = ctk.CTkLabel(
            self.sidebar,
            text="AwakeSense",
            font=("Poppins", 34, "bold"),
            text_color=PRIMARY
        )

        title.pack(
            pady=(30, 15)
        )

        # =========================
        # CLOCK
        # =========================

        self.clock = ClockWidget(
            self.sidebar
        )

        self.clock.pack(
            pady=(0, 18)
        )

        # =========================
        # DASHBOARD LABELS
        # =========================

        self.labels = {}

        items = [
            "👀 Eyes",
            "😉 Blinks",
            "🥱 Yawns",
            "🧠 Head",
            "📱 Phone",
            "😴 Fatigue",
            "💗 Status"
        ]

        for item in items:

            card = ctk.CTkFrame(
                self.sidebar,
                fg_color=SECONDARY,
                corner_radius=18,
                height=48
            )

            card.pack(
                fill="x",
                padx=20,
                pady=5
            )

            card.pack_propagate(False)

            label = ctk.CTkLabel(
                card,
                text=f"{item} : --",
                font=("Poppins", 16, "bold"),
                text_color=TEXT,
                anchor="w"
            )

            label.pack(
                fill="both",
                padx=18,
                pady=10
            )

            self.labels[item] = label

        # =========================
        # FATIGUE TITLE
        # =========================

        fatigue_title = ctk.CTkLabel(
            self.sidebar,
            text="Fatigue Level",
            font=("Poppins", 20, "bold"),
            text_color=PRIMARY
        )

        fatigue_title.pack(
            pady=(15, 8)
        )

        # =========================
        # FATIGUE PROGRESS
        # =========================

        self.progress = ctk.CTkProgressBar(
            self.sidebar,
            width=330,
            height=20,
            corner_radius=25,
            progress_color=PRIMARY,
            fg_color="#ECECEC"
        )

        self.progress.pack(
            pady=(0, 10)
        )

        self.progress.set(0)

        # =========================
        # FOOTER
        # =========================

        footer = ctk.CTkLabel(
            self.sidebar,
            text="Designed by Srihitha",
            font=("Poppins", 13),
            text_color=TEXT
        )

        footer.pack(
            side="bottom",
            pady=20
        )

        # =========================
        # DASHBOARD
        # =========================

        self.dashboard = DashboardUpdater(
            self
        )

        self.dashboard.update(
            "OPEN",
            0,
            0,
            "FORWARD",
            False,
            0,
            "READY"
        )

        # =========================
        # EMERGENCY OVERLAY
        # =========================

        self.emergency = ctk.CTkFrame(
            self,
            fg_color="#B00020",
            corner_radius=0
        )

        self.warning = ctk.CTkLabel(
            self.emergency,
            text=(
                "🚨\n\n"
                "DROWSINESS DETECTED\n\n"
                "WAKE UP!\n"
                "PLEASE TAKE A BREAK"
            ),
            font=("Poppins", 42, "bold"),
            text_color="white",
            justify="center"
        )

        self.warning.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.flash_state = False

        self.emergency.place_forget()

        # =========================
        # START CAMERA PROCESSING
        # =========================

        self.processor = FrameProcessor()

        self.live_camera = LiveCamera(
            self,
            self.camera,
            self.processor,
            self.dashboard
        )

    # =========================
    # SHOW EMERGENCY
    # =========================

    def show_emergency(self):

        if not self.emergency.winfo_ismapped():

            self.emergency.place(
                relx=0,
                rely=0,
                relwidth=1,
                relheight=1
            )

            self.flash_state = False

            self.flash()

    # =========================
    # HIDE EMERGENCY
    # =========================

    def hide_emergency(self):

        if self.emergency.winfo_ismapped():

            self.emergency.place_forget()

    # =========================
    # FLASH EMERGENCY
    # =========================

    def flash(self):

        if not self.emergency.winfo_ismapped():

            return

        if self.flash_state:

            self.emergency.configure(
                fg_color="#FF0000"
            )

        else:

            self.emergency.configure(
                fg_color="#B00020"
            )

        self.flash_state = not self.flash_state

        self.after(
            500,
            self.flash
        )