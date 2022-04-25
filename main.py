import pygame
import os
import random

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Dino:
RUNNING = [pygame.image.load("Assets\Dino\DinoRun1.png"),
            pygame.image.load("Assets\Dino\DinoRun2.png")]
JUMPING  = pygame.image.load("Assets\Dino\DinoJump.png")
DUCKING = [pygame.image.load("Assets\Dino\DinoDuck1.png"),
            pygame.image.load("Assets\Dino\DinoDuck2.png")]


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

class Dino:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.duck_img = DUCKING

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index+=1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index+=1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))




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