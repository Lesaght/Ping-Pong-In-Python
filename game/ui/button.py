import pygame
from .colors import Colors

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.is_hovered = False
        self.animation_offset = 0
        
    def draw(self, screen, animation):
        # Calculate hover effect
        hover_offset = 10 if self.is_hovered else 0
        
        # Calculate pulsing effect
        pulse = animation.get_pulse(0.8, 1.0)
        glow_size = int(self.rect.width * 0.1 * pulse)
        
        # Draw glow effect when hovered
        if self.is_hovered:
            glow_rect = self.rect.inflate(glow_size, glow_size)
            pygame.draw.rect(screen, Colors.NEON_BLUE, glow_rect, border_radius=10)
        
        # Draw main button
        color = Colors.NEON_BLUE if self.is_hovered else Colors.WHITE
        pygame.draw.rect(screen, color, self.rect, 2, border_radius=8)
        
        # Draw text with shadow
        text_surface = self.font.render(self.text, True, color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Add hover offset to text
        text_rect.y -= hover_offset
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False