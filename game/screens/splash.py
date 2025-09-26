from game.screens import BaseScreen, ScreenManager
from game.constants import COLORS, FONTS
import pygame


class SplashScreen(BaseScreen):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(FONTS["display"], 32)
        self.text = self.font.render(
            "OFF & SENGE PREZENTUJĄ", True, COLORS["MEDIUM_GRAY"]
        )

    def render(self, screen):
        if self.passed_since_activation(2000):
            ScreenManager.set("menu")

        screen.fill(COLORS["DARK_GRAY"])

        text_rect = self.text.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2)
        )

        screen.blit(self.text, text_rect)
