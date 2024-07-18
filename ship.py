import pygame
class Ship:
    """a class to hold ship and ship's properties"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # loading the ship
        self.image_of_ship = pygame.image.load("DurrrSpaceShip.bmp")
        self.rect = self.image_of_ship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.explosions = pygame.image.load("Screenshot-_71_.bmp")
        self.rest_of_explosions = self.explosions.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        self.screen.blit(self.image_of_ship, self.rect)

    def centre_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.x = float(self.rect.x)


    def ship_mover(self):
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.x += self.settings.ship_speed
            elif self.moving_left and self.rect.left > self.screen_rect.left:
                self.rect.x -= self.settings.ship_speed
            elif self.moving_up:
                self.rect.y -= self.settings.ship_speed
            elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += self.settings.ship_speed