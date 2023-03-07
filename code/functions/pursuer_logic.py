from functions import functions as fn

def pursuer_logic(pursuers, evader):
    print(fn.pursuer_distance(pursuers))
    print(fn.pursuer_angle(pursuers))
    for pursuer in pursuers:
        distance = fn.distance(pursuer, evader)
        if distance > 0:
            pursuer['velocity'][0] = 5 * (evader['rect'].centerx - pursuer['rect'].centerx) / distance
            pursuer['velocity'][1] = 5 * (evader['rect'].centery - pursuer['rect'].centery) / distance
    return pursuers