import pygame
import random

CLOUD = pygame.image.load("Assets\Others\Cloud.png")


class Cloud:
    def __init__(self, game_speed, SCREEN_WIDTH):
        self.game_speed = game_speed
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.y = random.randint(50,100)
        self.image = CLOUD
        self.width = self.image.get_width()
        self.x = SCREEN_WIDTH + random.randint(800,1000)

    def update(self):
        self.x -= self.game_speed["speed"]
        if self.x < -self.width:
            self.x = self.SCREEN_WIDTH + random.randint(2500,3000)
            self.y =  random.randint(50,100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
