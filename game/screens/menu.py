from game.screens import BaseScreen
from game.constants import COLORS


class MenuScreen(BaseScreen):
    def __init__(self):
        super().__init__()

    def render(self, screen):
        screen.fill(COLORS["BLACK"])
