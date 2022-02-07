import pygame

from .config import RECT_HEIGHT, RECT_WIDTH, RED, WIN_HEIGHT


class Player:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT)

    def draw(self):
        pygame.draw.rect(self.screen, RED, self.rect)

    def move(self, direction):
        old_position = self.rect.y
        if direction == 'UP':
            old_position = self.rect.y
            self.rect.y -= 4
        elif direction == 'DOWN':
            old_position = self.rect.y
            self.rect.y += 4
        if self.is_out_of_screen():
            self.rect.y = old_position

    def is_out_of_screen(self):
        if self.rect.bottom >= WIN_HEIGHT or self.rect.top <= 0:
            return True
