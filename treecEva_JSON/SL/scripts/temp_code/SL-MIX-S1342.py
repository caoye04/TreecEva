import math
from collections import defaultdict

def encode_command(direction, distance):
    return f"{direction}:{distance}".encode('utf-8')

def decode_command(encoded_cmd):
    return encoded_cmd.decode('utf-8').split(':')

class RoboticArmController:
    def __init__(self):
        self.x, self.y = 0.0, 0.0
        self.visited_positions = set()
        self.precision_scores = defaultdict(float)
        
    def move(self, direction, distance):
        if direction == 'N':
            self.y += float(distance)
        elif direction == 'S':
            self.y -= float(distance)
        elif direction == 'E':
            self.x += float(distance)
        elif direction == 'W':
            self.x -= float(distance)
        
        position = (round(self.x, 2), round(self.y, 2))
        self.visited_positions.add(position)
        self.precision_scores[position] = math.sqrt(self.x**2 + self.y**2)
        
    def process_commands(self, command_list):
        for cmd in command_list:
            decoded = decode_command(cmd)
            self.move(decoded[0], decoded[1])
        
    def calculate_final_score(self):
        unique_x_coords = {pos[0] for pos in self.visited_positions}
        unique_y_coords = {pos[1] for pos in self.visited_positions}
        coord_intersection = unique_x_coords & unique_y_coords
        
        score_sum = sum(self.precision_scores[pos] for pos in self.visited_positions)
        return round(score_sum * len(coord_intersection) / max(1, len(self.visited_positions)), 3)

# Initialize controller
arm_controller = RoboticArmController()

# Encoded movement commands
commands = [
    encode_command('N', 3.5),
    encode_command('E', 2.1),
    encode_command('S', 1.2),
    encode_command('W', 0.9),
    encode_command('N', 2.3),
    encode_command('E', 1.7)
]

# Process all commands
arm_controller.process_commands(commands)

# Calculate final precision score
final_precision_score = arm_controller.calculate_final_score()
print(f"Result: {final_precision_score}")