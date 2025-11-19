from collections import defaultdict

class CommandNode:
    def __init__(self, op_type, value):
        self.op_type = op_type
        self.value = value
        self.next = None

class RoboticArmController:
    def __init__(self):
        self.position_register = 0
        self.orientation_register = 0
        self.state = 'IDLE'
        self.command_freq = defaultdict(int)
    
    def process_commands(self, head):
        current = head
        while current:
            self.command_freq[current.op_type] += 1
            if current.op_type == 'MOVE':
                self.state = 'MOVING'
                self.position_register += current.value
            elif current.op_type == 'ROTATE':
                self.state = 'ROTATING'
                self.orientation_register ^= current.value
            current = current.next
        self.state = 'IDLE'
        return self.orientation_register

# Build command linked list
commands = [
    CommandNode('MOVE', 5),
    CommandNode('ROTATE', 3),
    CommandNode('MOVE', 2),
    CommandNode('ROTATE', 6),
    CommandNode('MOVE', 1)
]

for i in range(len(commands)-1):
    commands[i].next = commands[i+1]

controller = RoboticArmController()
final_orientation = controller.process_commands(commands[0])
print(f'Result: {final_orientation}')