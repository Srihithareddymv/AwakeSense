import pygame
import os


class Alarm:

    def __init__(self):

        pygame.mixer.init()

        sound_path = os.path.join(
            "assets",
            "sounds",
            "alarm.wav"
        )

        self.sound = pygame.mixer.Sound(sound_path)

        self.playing = False

    def play(self):

        if not self.playing:

            self.sound.play(-1)

            self.playing = True

    def stop(self):

        if self.playing:

            self.sound.stop()

            self.playing = False