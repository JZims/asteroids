import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # This already sets position, velocity, and radius!
        
    def draw(self, surface):  # Need surface parameter
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    