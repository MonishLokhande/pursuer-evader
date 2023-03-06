import math

# Define distance between two entities
def distance(a,b):
    return math.sqrt((a['rect'].centerx - b['rect'].centerx)**2 + (a['rect'].centery - b['rect'].centery)**2)