import pygame
from .ui.colors import Colors
from .ui.button import Button
from .ui.animations import Animation

class MainMenu:
    def __init__(self):
        self.animation = Animation()
        button_width = 200
        button_height = 50
        button_spacing = 20
        
        # Center buttons horizontally and vertically
        start_y = 300
        
        self.ai_button = Button(
            400 - button_width // 2,
            start_y,
            button_width,
            button_height,
            "Play with AI"
        )
        
        self.pvp_button = Button(
            400 - button_width // 2,
            start_y + button_height + button_spacing,
            button_width,
            button_height,
            "Player vs Player"
        )
        
        # Load and scale background pattern
        self.bg_pattern = self.create_background_pattern()
        self.title_font = pygame.font.Font(None, 120)

    def create_background_pattern(self):
        pattern = pygame.Surface((20, 20))
        pygame.draw.line(pattern, Colors.GRAY, (10, 0), (10, 20), 1)
        return pattern

    def draw_background(self, screen):
        # Tile the background pattern
        for x in range(0, 800, 20):
            for y in range(0, 600, 20):
                screen.blit(self.bg_pattern, (x, y))

    def draw_title(self, screen):
        # Draw glowing PONG title
        glow_offset = self.animation.get_sine_wave(amplitude=3)
        glow_size = abs(int(glow_offset * 2))
        
        title_text = "PONG"
        
        # Draw outer glow
        for offset in range(glow_size, 0, -1):
            alpha = int(255 * (1 - offset / glow_size))
            glow_surface = self.title_font.render(title_text, True, Colors.NEON_BLUE)
            glow_surface.set_alpha(alpha)
            text_rect = glow_surface.get_rect(center=(400, 150))
            text_rect.y += glow_offset
            screen.blit(glow_surface, text_rect)
        
        # Draw main title
        title_surface = self.title_font.render(title_text, True, Colors.WHITE)
        title_rect = title_surface.get_rect(center=(400, 150))
        title_rect.y += glow_offset
        screen.blit(title_surface, title_rect)

    def handle_events(self, events):
        for event in events:
            if self.ai_button.handle_event(event):
                return "AI"
            if self.pvp_button.handle_event(event):
                return "PVP"
        return None

    def draw(self, screen):
        screen.fill(Colors.BLACK)
        
        # Update animation
        self.animation.update()
        
        # Draw background pattern
        self.draw_background(screen)
        
        # Draw title with glow effect
        self.draw_title(screen)
        
        # Draw buttons
        self.ai_button.draw(screen, self.animation)
        self.pvp_button.draw(screen, self.animation)
        
        pygame.display.flip()