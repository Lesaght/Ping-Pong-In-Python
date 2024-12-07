import pygame
from .constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE,
    PADDLE_MARGIN, SCORE_FONT_SIZE, WINNING_SCORE
)
from .paddle import Paddle
from .ball import Ball
from .menu import MainMenu
from .game_state import GameState
from .ai import AI

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ping Pong")
        self.clock = pygame.time.Clock()
        
        self.game_state = GameState.MENU
        self.menu = MainMenu()
        self.reset_game()
        self.running = True
        self.ai_mode = False

    def reset_game(self):
        self.player = Paddle(PADDLE_MARGIN)
        self.opponent = Paddle(WINDOW_WIDTH - PADDLE_MARGIN)
        self.ball = Ball()
        self.ai = AI(self.opponent, self.ball)
        self.game_font = pygame.font.Font(None, SCORE_FONT_SIZE)

    def handle_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        if self.game_state == GameState.MENU:
            choice = self.menu.handle_events(events)
            if choice == "AI":
                self.ai_mode = True
                self.game_state = GameState.PLAYING
            elif choice == "PVP":
                self.ai_mode = False
                self.game_state = GameState.PLAYING
        
        elif self.game_state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.move_up()
            if keys[pygame.K_s]:
                self.player.move_down()
            
            # Only allow opponent controls in PVP mode
            if not self.ai_mode:
                if keys[pygame.K_UP]:
                    self.opponent.move_up()
                if keys[pygame.K_DOWN]:
                    self.opponent.move_down()

    def update(self):
        if self.game_state == GameState.PLAYING:
            self.ball.move()

            # Update AI if in AI mode
            if self.ai_mode:
                self.ai.update()

            # Ball collision with paddles
            if self.ball.rect.colliderect(self.player.rect) or \
               self.ball.rect.colliderect(self.opponent.rect):
                self.ball.speed_x *= -1

            # Score points
            if self.ball.rect.left <= 0:
                self.opponent.score += 1
                self.ball.reset()
            if self.ball.rect.right >= WINDOW_WIDTH:
                self.player.score += 1
                self.ball.reset()

            # Check for game over
            if self.player.score >= WINNING_SCORE or self.opponent.score >= WINNING_SCORE:
                self.game_state = GameState.MENU
                self.reset_game()

    def draw(self):
        if self.game_state == GameState.MENU:
            self.menu.draw(self.screen)
        
        elif self.game_state == GameState.PLAYING:
            self.screen.fill(BLACK)
            
            # Draw center line
            pygame.draw.aaline(self.screen, WHITE, 
                             (WINDOW_WIDTH // 2, 0),
                             (WINDOW_WIDTH // 2, WINDOW_HEIGHT))
            
            # Draw scores
            player_score = self.game_font.render(str(self.player.score), True, WHITE)
            opponent_score = self.game_font.render(str(self.opponent.score), True, WHITE)
            
            self.screen.blit(player_score, (WINDOW_WIDTH // 4, 20))
            self.screen.blit(opponent_score, (3 * WINDOW_WIDTH // 4, 20))

            self.player.draw(self.screen)
            self.opponent.draw(self.screen)
            self.ball.draw(self.screen)
            
            pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()