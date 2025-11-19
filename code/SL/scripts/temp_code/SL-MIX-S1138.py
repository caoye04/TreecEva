from collections import defaultdict

class VacuumRobot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.state = 'IDLE'
    
    def move(self, direction):
        if direction == 'N':
            self.y += 1
        elif direction == 'S':
            self.y -= 1
        elif direction == 'E':
            self.x += 1
        elif direction == 'W':
            self.x -= 1
        self.state = 'MOVING'
    
    def get_position(self):
        return (self.x, self.y)

# Movement sequence
commands = ['N', 'E', 'E', 'S', 'W', 'N']
robot = VacuumRobot()

for cmd in commands:
    robot.move(cmd)

final_x, final_y = robot.get_position()
manhattan_distance = abs(final_x) + abs(final_y)
print(f'Result: {manhattan_distance}')