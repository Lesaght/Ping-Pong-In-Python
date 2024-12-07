import math
import pygame

class Animation:
    def __init__(self):
        self.time = 0
    
    def update(self):
        self.time = (self.time + 0.016) % (2 * math.pi)  # 60 FPS approximation
    
    def get_sine_wave(self, amplitude=1.0, frequency=1.0):
        return math.sin(self.time * frequency) * amplitude
    
    def get_pulse(self, min_value=0.8, max_value=1.0):
        return min_value + (max_value - min_value) * (math.sin(self.time * 2) * 0.5 + 0.5)