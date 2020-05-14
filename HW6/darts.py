from math import sqrt

"""

Good inputs: (10.5, 3.0), (1, 0), (45, 11)

Bad inputs: (1+4i, 2-i), 'sandwich'

Edge cases: (0, 0), (math.inf, 0)

"""

def darts_score(hitpos_x, hitpos_y):
    hit_distance = sqrt(hitpos_x^2 + hitpos_y^2)
    if hit_distance < 0:
        raise Exception("The dartboard should not be placed on a complex hyperplane.")
    elif hit_distance < 1:
        return 10
    elif hit_distance < 5:
        return 5
    elif hit_distance < 10:
        return 1
    else:
        return 0