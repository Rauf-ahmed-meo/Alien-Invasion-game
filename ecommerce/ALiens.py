# alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        original_image = pygame.image.load('ship3.bmp')
        # Specify the desired size (width, height) for the alien image.
        new_size = (50, 50)
        self.image = pygame.transform.scale(original_image, new_size)

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x