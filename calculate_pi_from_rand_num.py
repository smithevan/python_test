#recreating solution to problem found online with a few modifications 
#Given a random set of numbers, determine pi: following along with example on youtube
import math
import random 

def estimate_pi(points):
    points_in_circle = 0
    points_in_square = 0
    for i in range(points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance_point_to_origin = math.sqrt(x**2 + y**2)
        if distance_point_to_origin <= 1:
            points_in_circle += 1
        points_in_square += 1

    result = 4 * points_in_circle/points_in_square
    return result

sample_set = int(input('Input Number:'))
print(estimate_pi(sample_set))


