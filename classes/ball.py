import pygame

from .config import BALL_HEIGHT, BALL_WIDTH, BLUE, WIN_HEIGHT, WIN_WIDTH, DIRECTION_X, DIRECTION_Y


class Ball:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, BALL_WIDTH, BALL_HEIGHT)
        self.directions = {
            'LEFT': [-4, 0],
            'RIGHT': [4, 0],
            'TOP_LEFT': [-4, -4],
            'TOP_RIGHT': [4, -4],
            'BOTTOM_LEFT': [-4, 4],
            'BOTTOM_RIGHT': [4, 4]
        }

    def draw(self):
        pygame.draw.rect(self.screen, BLUE, self.rect)

    def move(self, x, y):
        self.rect.move_ip(x, y)

    def is_out_of_screen(self):
        if self.rect.x <= 0 or self.rect.right >= WIN_WIDTH:
            return True

    def is_bouncing(self):
        if self.rect.y <= 0 + 10 or self.rect.y >= WIN_HEIGHT - 10:
            return True

    def save_side_position(self):
        if self.rect.x < WIN_WIDTH/2:
            return 'LEFT'
        elif self.rect.x > WIN_WIDTH/2:
            return 'RIGHT'

    def save_wall_position(self):
        if self.rect.top <= 0:
            return 'TOP'
        elif self.rect.bottom >= WIN_HEIGHT:
            return 'BOTTOM'

    def collide_player(self, left_player, right_player):
        if self.rect.colliderect(left_player) or \
                self.rect.colliderect(right_player):
            return True
