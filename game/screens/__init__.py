import pygame


class BaseScreen:
    def __init__(self):
        self.active = False
        self.last_activated_at = None
        if type(self) is BaseScreen:
            raise Exception(
                "BaseScreen is an abstract class and cannot be instantiated directly"
            )

    def render(self, screen: pygame.Surface):
        raise NotImplementedError("render method unimplemented")

    def passed_since_activation(self, ticks: int):
        return pygame.time.get_ticks() - self.last_activated_at >= ticks


class ScreenManager(object):
    current_screen = ""
    screens: dict[str, BaseScreen] = {}

    @staticmethod
    def add(name: str, screen: BaseScreen):
        ScreenManager.screens[name] = screen

    @staticmethod
    def set(name: str):
        if ScreenManager.screens.get(ScreenManager.current_screen):
            ScreenManager.screens[ScreenManager.current_screen].active = False

        ScreenManager.current_screen = name

        ScreenManager.screens[name].active = True
        ScreenManager.screens[name].last_activated_at = pygame.time.get_ticks()

    @staticmethod
    def next():
        return ScreenManager.screens[ScreenManager.current_screen]
