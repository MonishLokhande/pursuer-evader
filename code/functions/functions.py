import math
import numpy as np

# Define distance between two entities
def distance(a,b):
    return math.sqrt((a['rect'].centerx - b['rect'].centerx)**2 + (a['rect'].centery - b['rect'].centery)**2)

# Define distance between all pursuers
def pursuer_distance(pursuers):
    length = len(pursuers)
    pursuer_distance = np.zeros((length,length))
    for i in range(len(pursuers)):
        for j in range(len(pursuers)):
            pursuer_distance[i][j] = distance(pursuers[i], pursuers[j])
    return pursuer_distance

# Define angle between all pursuers
def pursuer_angle(pursuers):
    length = len(pursuers)
    pursuer_angle = np.zeros((length,length))
    for i in range(len(pursuers)):
        for j in range(len(pursuers)):
            pursuer_angle[i][j] = math.atan2(pursuers[i]['rect'].centery - pursuers[j]['rect'].centery, pursuers[i]['rect'].centerx - pursuers[j]['rect'].centerx)
    return pursuer_angle
