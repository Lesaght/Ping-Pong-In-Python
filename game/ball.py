import pygame
from .constants import BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y, WINDOW_WIDTH, WINDOW_HEIGHT
from .physics import get_initial_ball_velocity, handle_wall_collision

class Ball:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2,
                              WINDOW_HEIGHT // 2 - BALL_SIZE // 2,
                              BALL_SIZE, BALL_SIZE)
        self.speed_x, self.speed_y = get_initial_ball_velocity(BALL_SPEED_X, BALL_SPEED_Y)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top and bottom using physics utility
        self.speed_y = handle_wall_collision(self.rect.y, self.speed_y, WINDOW_HEIGHT - BALL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)