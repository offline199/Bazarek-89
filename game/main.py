import pygame
from game.constants import COLORS, RESOLUTION, NAME
from game.screens import ScreenManager
from game.screens.splash import SplashScreen
from game.screens.menu import MenuScreen


# Initialize Pygame
def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption(NAME)

    clock = pygame.time.Clock()

    # Add screens
    ScreenManager.add("splash", SplashScreen())
    ScreenManager.add("menu", MenuScreen())

    ScreenManager.set("splash")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        # screen.fill(COLORS["black"])

        # Rendering goes here
        ScreenManager.next().render(screen)

        # FPS
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
