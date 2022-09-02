import pygame
import random
from Dino import Dino
from Cloud import Cloud
from sys import exit

game_speed = {"speed": 14}

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load("Assets\Dino\DinoRun1.png"),
            pygame.image.load("Assets\Dino\DinoRun2.png")]

#Cactus:
SMALL_CACTUS = [pygame.image.load("Assets\Cactus\SmallCactus1.png"),
                pygame.image.load("Assets\Cactus\SmallCactus2.png"),
                pygame.image.load("Assets\Cactus\SmallCactus3.png")]
LARGE_CACTUS = [pygame.image.load("Assets\Cactus\LargeCactus1.png"),
                pygame.image.load("Assets\Cactus\LargeCactus2.png"),
                pygame.image.load("Assets\Cactus\LargeCactus3.png")]

#Bird:
BIRD = [pygame.image.load("Assets\Bird\Bird1.png"),
        pygame.image.load("Assets\Bird\Bird2.png")]

#Others:

BG = pygame.image.load("Assets\Others\Track.png")

class Enemy:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed["speed"]
        if self.rect.x < -self.rect.width:
            enemies.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallCactus(Enemy):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Enemy):
    def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Enemy):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index+=1

def main():
    global x_pos_bg, y_pos_bg, points, enemies
    run = True
    clock = pygame.time.Clock()
    player = Dino()
    cloud = Cloud(game_speed, SCREEN_WIDTH)
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    enemies = []
    death_count = 0

    def score():
        global points
        points+=1
        if points % 100 == 0:
            game_speed["speed"]+=1

        text = font.render("Points: "+str(points), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (1000,40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed["speed"]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(enemies) == 0:
            if random.randint(0,2) == 0:
                enemies.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0,2) == 1:
                enemies.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0,2) == 2:
                enemies.append(Bird(BIRD))

        for enemy in enemies:
            enemy.draw(SCREEN)
            enemy.update()
            if player.dino_rect.colliderect(enemy.rect):
                pygame.time.delay(1000)
                death_count+=1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255,255,255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0,0,0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0,0,0))
            score = font.render("Your Score: "+str(points), True, (0,0,0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2-20, SCREEN_HEIGHT // 2-140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
        