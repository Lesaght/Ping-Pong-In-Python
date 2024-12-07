import pygame

# Color definitions with RGB values
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    NEON_BLUE = (0, 255, 255)
    NEON_PINK = (255, 20, 147)
    GRAY = (150, 150, 150)
    
    @staticmethod
    def get_gradient(start_color, end_color, progress):
        """Create a color gradient between two colors"""
        return tuple(
            int(start + (end - start) * progress)
            for start, end in zip(start_color, end_color)
        )