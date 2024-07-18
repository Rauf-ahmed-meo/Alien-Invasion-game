import pygame
import sys
from settings import Settings
from ship import Ship
from bullets import Bullet
from ALiens import Alien
from game_stats import Gamestats
from time import sleep
from buttons import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('ALine Invasion')
        self.bg_color = self.settings.bg_color
        self.clock = pygame.Clock()
        self.stats = Gamestats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = False
        self.play_button = Button(self, "play")
        self.sb = Scoreboard(self)
    def _create_fleet(self):
        """making a alien"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width

            current_x = alien_width
            current_y += alien_height
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.centre_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:

                self._update_aliens()
                self.bullets.update()
                self._update_bullets()
                self.sb.show_score()
            self._update_screen()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1


    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self.aliens_reach_the_bottom()

    def _update_bullets(self):
        # Update bullets
        self.bullets.update()

        # Remove bullets that have gone off the screen
        self.bullets = pygame.sprite.Group(
            [bullet for bullet in self.bullets.sprites() if bullet.rect.bottom > 0])

        # Perform collisions
        self._check_bullet_alien_collision()
    def _check_bullet_alien_collision(self):
        if self.aliens:
            collisions = pygame.sprite.groupcollide(
                self.aliens, self.bullets, True, True)
            if collisions:
                for aliens in collisions.values():
                    self.stats.score += self.settings.alien_points * len(aliens)
                    self.sb.prep_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def aliens_reach_the_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            self._check_key_down_events(event)
            self._check_key_up_events(event)

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
    def _check_key_down_events(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_UP:
                self.ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                self._fire_bullets()

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
                self.game_active = True
                self.ship.centre_ship()
                self.aliens.empty()
                self._create_fleet()
                self.stats.reset_stats()
                self.sb.prep_score()
                pygame.mouse.set_visible(False)
                self.settings.initialize_dynamic_settings()
    def _check_key_up_events(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_UP:
                self.ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.ship.ship_mover()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.clock.tick(60)
        if not self.game_active:
            self.play_button.draw_button()
        self.sb.show_score()
        pygame.display.flip()  # Move the flip() call to the end


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
