#Given a random set of numbers, determine pi: following along with example on youtube
import from math sqrt

def estimate_pi(points):
    points_in_circle = 0
    points_in_square = 0
    for i in range(points):
        x = random.random(0, 1)
        y = random.random(0, 1)
        distance_point_to_origin = sqrt(x**2 + y**2)
        if distance_point_to_origin <= 1:
            points_in_circle += 1
        points_in_square += 1

    return 4 * points_in_circle/points_in_square



