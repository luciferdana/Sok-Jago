import pygame
from abc import ABC, abstractmethod

Yellow = (255, 255, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Blue = (0,0, 255)
Green = (0, 255, 0)

class AbstrakHealthbar(ABC):
    def __init__(self, health):
        self.health = int(health)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class HealthBarAgus(AbstrakHealthbar):
    def __init__(self, health):
        super().__init__(health)
        self.full_health = int(health)
        self.ratio = self.health / self.full_health

    def update(self, health):
        self.health = health
        self.ratio = self.health / self.full_health

    def draw(self, screen, x, y):
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))
       pygame.draw.rect(screen, Red, (x, y, 400, 30))
       pygame.draw.rect(screen, Yellow, (x, y, 400 * self.ratio, 30)) 
    
class HealthBarIca(AbstrakHealthbar):
    def __init__(self, health):
        super().__init__(health)
        self.full_health = int(health)
        self.ratio = self.health / self.full_health
    
    def update(self, health):
        self.health = health
        self.ratio = self.health / self.full_health

    def draw(self, screen, x, y):
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))
       pygame.draw.rect(screen, Red, (x, y, 400, 30))
       pygame.draw.rect(screen, Green, (x, y, 400 * self.ratio, 30))

class HealthBarSamson(AbstrakHealthbar):
    def __init__(self, health):
        super().__init__(health)
        self.full_health = int(health)
        self.ratio = self.health / self.full_health
    
    def update(self, health):
        self.health = health
        self.ratio = self.health / self.full_health

    def draw(self, screen, x, y):
       pygame.draw.rect(screen, White, (x - 2, y - 2, 405, 34))
       pygame.draw.rect(screen, Red, (x, y, 400, 30))
       pygame.draw.rect(screen, Blue, (x, y, 400 * self.ratio, 30))
