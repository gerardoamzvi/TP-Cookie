from numpy import sqrt, cos, pi
def distance_x_y(x, y):
    return (y[0]* 0.25 - x[0]* 0.25)**2 + (y[1]* 0.25 - x[1]* 0.25)**2 


def equa_diff(t):
    return sqrt(284.5 * cos(t) + 64 * pi**2)
