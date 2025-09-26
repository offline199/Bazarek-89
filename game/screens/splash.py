from game.screens import BaseScreen, ScreenManager
from game.constants import COLORS, FONTS, SOUNDS
import pygame


class SplashScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(FONTS["display"], 32)
        self.text = self.font.render(
            "OFF & SENGE PREZENTUJĄ", True, COLORS["MEDIUM_GRAY"]
        )

        self.sound = pygame.mixer.Sound(SOUNDS["start"])
        self.played_sound = False

    def render(self, screen):
        if self.passed_since_activation(2000):
            ScreenManager.set("menu")

        if not self.played_sound:
            self.played_sound = True
            self.sound.play()  # 🔊 Play sound here

        screen.fill(COLORS["DARK_GRAY"])
        text_rect = self.text.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2)
        )
        screen.blit(self.text, text_rect)
