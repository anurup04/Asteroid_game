import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self,other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance <= (self.radius + other.radius):
            return True
        else:
            return  False

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y,SHOT_RADIUS)
        self.velocity = velocity

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,SHOT_RADIUS,2)
    
    def update(self,dt):
        self.position += (self.velocity * dt) 

    