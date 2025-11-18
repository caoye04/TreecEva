from collections import defaultdict
import itertools

class CommandNode:
    def __init__(self, command, next_node=None):
        self.command = command
        self.next = next_node

def process_commands(start_pos, command_chain):
    current_pos = start_pos
    node = command_chain
    while node:
        cmd = node.command
        if cmd.startswith('ROT'):
            angle = int(cmd[3:])
            current_pos = (current_pos + angle) % 360
        elif cmd.startswith('REV'):
            times = int(cmd[3:])
            current_pos = (current_pos * times) % 180
        node = node.next
    return current_pos

# Build linked list of commands
commands = ['ROT45', 'REV3', 'ROT180', 'REV2']
head = None
for cmd in reversed(commands):
    head = CommandNode(cmd, head)

# Process commands with initial position
initial_position = 30
final_position = process_commands(initial_position, head)

print(f"Result: {final_position}")