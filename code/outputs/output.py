import numpy as np

def energy(pursuers):
    energy = 0
    for pursuer in pursuers:
        energy += np.linalg.norm(pursuer['velocity'])**2
    return energy