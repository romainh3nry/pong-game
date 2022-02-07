import random

import pygame

from .ball import Ball
from .config import (DIRECTION_X, DIRECTION_Y, RECT_X, RECT_Y, WIN_HEIGHT,
                     WIN_WIDTH)
from .player import Player


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("PONG")
        self.running = True
        self.rect_left = Player(RECT_X, RECT_Y, self.screen)
        self.rect_right = Player(WIN_WIDTH - RECT_X, RECT_Y, self.screen)
        self.ball = Ball(WIN_WIDTH/2, WIN_HEIGHT/2, self.screen)
        self.clock = pygame.time.Clock()
        self.ball_position = None
        self.ball_x = DIRECTION_X
        self.ball_y = DIRECTION_Y

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect_left.move('UP')
            self.rect_right.move('UP')
        elif pressed[pygame.K_DOWN]:
            self.rect_left.move('DOWN')
            self.rect_right.move('DOWN')

    def run(self):
        while self.running:
            self.clock.tick(50)
            self.screen.fill((0, 0, 0))
            self.handle_input()
            self.rect_left.draw()
            self.rect_right.draw()
            self.ball.draw()
            self.ball.move(self.ball_x, self.ball_y)

            if self.ball.is_out_of_screen():
                self.running = False

            if self.ball.is_bouncing():
                wall = self.ball.save_wall_position()
                if wall == 'TOP':
                    if self.ball_position == 'LEFT':
                        self.ball_x = 4
                        self.ball_y = 4
                    elif self.ball_position == 'RIGHT':
                        self.ball_x = -4
                        self.ball_y = 4
                elif wall == 'BOTTOM':
                    if self.ball_position == 'LEFT':
                        self.ball_x = 4
                        self.ball_y = -4
                    elif self.ball_position == 'RIGHT':
                        self.ball_x = -4
                        self.ball_y = -4

            if self.ball.collide_player(self.rect_left, self.rect_right):
                self.ball_position = self.ball.save_side_position()
                if self.ball_position == 'LEFT':
                    self.ball_x = 4
                    self.ball_y = random.choice([4, -4])
                elif self.ball_position == 'RIGHT':
                    self.ball_x = -4
                    self.ball_y = random.choice([4, -4])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
