import pygame
import random
import math
import time

# initialize PyGame
pygame.init()

# set up the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# set up the pursuers
pursuers = []
for i in range(3):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pursuer = {
        'rect': pygame.Rect(x, y, 20, 20),
        'velocity': [0, 0],
        'color': blue
    }
    pursuers.append(pursuer)

# set up the evader
evader = {
    'rect': pygame.Rect(screen_width/2, screen_height/2, 20, 20),
    'velocity': [0, 0],
    'color': red
}

# set up the clock
clock = pygame.time.Clock()

# Define distance between two entities
def distance(a,b):
    return math.sqrt((a['rect'].centerx - b['rect'].centerx)**2 + (a['rect'].centery - b['rect'].centery)**2)

# define the main game loop
def game_loop():
    # main game loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # move the evader randomly
        evader['velocity'][0] = random.randint(-5, 5)
        evader['velocity'][1] = random.randint(-5, 5)
        evader['rect'].move_ip(evader['velocity'])
        
        # move the pursuers towards the evader
        for pursuer in pursuers:
            d = distance(pursuer, evader)
            if d > 0:
                pursuer['velocity'][0] = 5 * (evader['rect'].centerx - pursuer['rect'].centerx) / d
                pursuer['velocity'][1] = 5 * (evader['rect'].centery - pursuer['rect'].centery) / d
            pursuer['rect'].move_ip(pursuer['velocity'])
        
        # draw the screen
        screen.fill(white)
        pygame.draw.rect(screen, evader['color'], evader['rect'])
        for pursuer in pursuers:
            pygame.draw.rect(screen, pursuer['color'], pursuer['rect'])
        pygame.display.flip()
        
        # limit the frame rate
        clock.tick(10)

        if (distance(pursuers[0],evader))*(distance(pursuers[1],evader))*(distance(pursuers[2],evader)) == 0:
            time.sleep(5)
            running = False

    # clean up PyGame
    pygame.quit()

# run the game loop
game_loop()