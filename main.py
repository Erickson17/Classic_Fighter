import pygame
from fighter import Fighter

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Clone")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colors
YELLOW = (255, 255, 0)
RED = (255, 0 , 0)
WHITE = (255, 255, 255)

#define fighter variables
WARRIOR_SIZE = 162
WARRIOR_DATA = [WARRIOR_SIZE]

#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#load spritesheets
warrior_sheet = pygame.image.load("assets/images/warrior/warrior.png").convert_alpha()
# wizard_sheet = pygame.image.load("assets/images/wizzard/wizard.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10,8,1,7,7,3,7]
# WIZARD_ANIMATION_STEPS = [8,8,1,8,8,3,7]

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#function for drawing health bars
def draw_health_bar(health, x, y):
    ratio = health / 100 
    pygame.draw.rect(screen , WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen , RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances of fighters
fighter_1 = Fighter(200, 310, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310)

#game loop
run = True 
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighter
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit pygame
pygame.quit()