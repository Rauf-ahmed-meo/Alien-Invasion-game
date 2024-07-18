import pygame.font
class Scoreboard:
    def __init__(self, ai_game):
        """initialize the score keeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        #font settings for scoring information
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()  # Call the prep_score method to initialize score_image

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,
        True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)