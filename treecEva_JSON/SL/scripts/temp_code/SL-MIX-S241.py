from collections import namedtuple
import math

# Define drone state using namedtuple
drone_state = namedtuple('drone_state', ['x', 'y'])

# Initial positions of drones
alpha_drone = drone_state(2.5, 3.7)
beta_drone = drone_state(-1.4, 5.2)
gamma_drone = drone_state(4.8, -2.1)

# Movement displacement vectors
alpha_displacement = (3.1, -2.6)
beta_displacement = (-2.7, 1.9)
gamma_displacement = (0.5, 4.3)

# Calculate final positions
final_alpha = drone_state(alpha_drone.x + alpha_displacement[0], alpha_drone.y + alpha_displacement[1])
final_beta = drone_state(beta_drone.x + beta_displacement[0], beta_drone.y + beta_displacement[1])
final_gamma = drone_state(gamma_drone.x + gamma_displacement[0], gamma_drone.y + gamma_displacement[1])

# Function to calculate distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Calculate side lengths of the triangle
side_a = euclidean_distance(final_alpha, final_beta)
side_b = euclidean_distance(final_beta, final_gamma)
side_c = euclidean_distance(final_gamma, final_alpha)

# Calculate semi-perimeter
semi_perimeter = (side_a + side_b + side_c) / 2.0

# Calculate area using Heron's formula
survey_zone_area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))

print(f"Result: {survey_zone_area}")