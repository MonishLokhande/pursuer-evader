import pygame

def agent(coordinates,velocity,color):
    agent = {
        'rect': pygame.Rect(coordinates[0], coordinates[1], 20, 20),
        'velocity': velocity,
        'color': color
    }
    return agent
