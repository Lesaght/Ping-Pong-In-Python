import pygame
from .constants import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, WINDOW_HEIGHT

class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, 
                              PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
        self.score = 0

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)