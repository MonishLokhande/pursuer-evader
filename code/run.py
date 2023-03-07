import pygame
import random
import time

from agents import agent as ag
from functions import functions as fn
from functions import pursuer_logic as pl

# Pygame
pygame.init()

# Screen
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Define the Pursuers
pursuers = []
for i in range(3):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pursuer = ag.agent([x,y],[0,0],blue)
    pursuers.append(pursuer)

# Define the Evader
evader = ag.agent([screen_width/2,screen_height/2],[0,0],red)

# Clock
clock = pygame.time.Clock()

# Game Loop
def game_loop():
    # Continuously run the loop till evader caught by pursuers
    running = True

    # Every Instance of the Game
    while running:
        # If the game is asked to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # move the evader randomly
        evader['velocity'][0] = random.randint(-5, 5)
        evader['velocity'][1] = random.randint(-5, 5)
        evader['rect'].move_ip(evader['velocity'])
        
        # Move Purser towards Evader (Main Logic of the Game)
        pl.pursuer_logic(pursuers, evader)
        for pursuer in pursuers:
            pursuer['rect'].move_ip(pursuer['velocity'])
        
        # Display the game
        screen.fill(white)
        pygame.draw.rect(screen, evader['color'], evader['rect'])
        for pursuer in pursuers:
            pygame.draw.rect(screen, pursuer['color'], pursuer['rect'])
        pygame.display.flip()
        
        # Frame Rate
        clock.tick(10)

        # If the evader is caught by any of the pursuers, stop the game
        if (fn.distance(pursuers[0],evader))*(fn.distance(pursuers[1],evader))*(fn.distance(pursuers[2],evader)) == 0:
            time.sleep(5)
            running = False

    # Quit the game
    pygame.quit()

# Run the Game
game_loop()