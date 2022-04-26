import pygame
from main import SCREEN_WIDTH, game_speed
import random

CLOUD = pygame.image.load("Assets\Others\Cloud.png")

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500,3000)
            self.y =  random.randint(50,100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
