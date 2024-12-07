import pygame
from .constants import WINDOW_HEIGHT, PADDLE_SPEED

class AI:
    def __init__(self, paddle, ball):
        self.paddle = paddle
        self.ball = ball
        self.reaction_delay = 2  # Makes AI beatable by adding some delay

    def update(self):
        # Only move if ball is moving towards AI
        if self.ball.speed_x > 0:
            # Predict where ball will be
            target_y = self.ball.rect.centery
            
            # Add some imperfection to make AI beatable
            if abs(self.paddle.rect.centery - target_y) > self.reaction_delay:
                if self.paddle.rect.centery < target_y:
                    self.paddle.move_down()
                if self.paddle.rect.centery > target_y:
                    self.paddle.move_up()