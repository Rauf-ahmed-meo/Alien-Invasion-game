class Settings:
    """settings for alien invasion (ai) game"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0,250,0)
        # settings for bullets
        self.bullet_speed = 5
        self.ship_speed = 7
        self.bullet_width = 15
        self.bullet_height = 50
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        # settings for alien
        self.alien_speed = 1
        self.alien_drop_speed = 10
        self.fleet_direction = 1
        #game stats
        self.speed_up_scale = 1.1
        self.ships_limit = 3
        self.alien_points = 50
    def initialize_dynamic_settings(self):
        self.alien_speed = 1
        self.alien_drop_speed = 10
        self.ship_speed = 7


    def increase_speed(self):
        self.alien_speed *= self.speed_up_scale
        self.ship_speed *= self.speed_up_scale
        self.alien_drop_speed *= self.speed_up_scale

