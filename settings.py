import pygame


class Settings:

    def __init__(self):
        """ Параметры экрана """
        self.screen_width = 1440
        self.screen_height = 770
        self.bg_color = (230, 230, 230)  #ОДНОТОННЫЙ ФОН
        # self.bg_color = pygame.image.load('images/backgr.png')

        """ Настройки корабля """
        self.ship_limit = 3

        """ Параметры снаряда """
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 5

        """ Настройки пришельцев """
        self.fleet_drop_speed = 10

        """ Темп ускорения игры """
        self.speedup_scale = 1.2

        """Темп роста стоимости пришельцев"""
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализирует настройки, изменяющиеся по ходу игры """
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.5  # 0.5

        self.fleet_direction = 1

        """Подсчет очков"""
        self.aliens_points = 50

    def increase_speed(self):
        """ Увеличивает настройки скорости """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)
