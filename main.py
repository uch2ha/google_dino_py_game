import pygame
import os
import random
from Dino import Dino

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



#Cactus:
SMALL_CACTUS = [pygame.image.load("Assets\Cactus\SmallCactus1.png"),
                pygame.image.load("Assets\Cactus\SmallCactus2.png"),
                pygame.image.load("Assets\Cactus\SmallCactus3.png")]
LARGE_CACTUS = [pygame.image.load("Assets\Cactus\LargeCactus1.png"),
                pygame.image.load("Assets\Cactus\LargeCactus2.png"),
                pygame.image.load("Assets\Cactus\LargeCactus3.png")]

#Bird:
Bird = [pygame.image.load("Assets\Bird\Bird1.png"),
        pygame.image.load("Assets\Bird\Bird2.png")]

#Others:
CLOUD = pygame.image.load("Assets\Others\Cloud.png")
BG = pygame.image.load("Assets\Others\Track.png")




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

def main():
    global game_speed, x_pos_bg, y_pos_bg
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    x_pos_bg = 380

    

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        cloud.draw(SCREEN)
        cloud.update()

        clock.tick(30)
        pygame.display.update()

main()