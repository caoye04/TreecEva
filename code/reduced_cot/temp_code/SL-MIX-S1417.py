from contextlib import contextmanager
from dataclasses import dataclass
from typing import List

def transform_command(cmd: int, depth: int) -> int:
    if depth == 0:
        return cmd
    # Bitwise transformations
    step1 = cmd ^ 0b10101010
    step2 = (step1 & 0b11110000) | ((step1 << 2) & 0b00001111)
    step3 = step2 >> 1
    return transform_command(step3, depth - 1)

def process_commands(command_sequence: List[int]) -> int:
    state_stack = []
    current_code = 0
    
    for i, cmd in enumerate(command_sequence):
        state_stack.append(current_code)
        transformed = transform_command(cmd, i % 3 + 1)
        current_code ^= transformed
        
        # Backtrack on error condition (simulated)
        if current_code & 0xF0 == 0x80:
            current_code = state_stack.pop()
    
    return current_code

@contextmanager
def command_context():
    print("Initializing command processor...")
    try:
        yield
    finally:
        print("Command processing complete.")

@dataclass
class CommandPacket:
    id: int
    payload: List[int]

# Main execution
with command_context():
    packet = CommandPacket(42, [0xC5, 0x3A, 0xF1, 0x09, 0xB2])
    final_command_code = process_commands(packet.payload)
    print(f"Result: {final_command_code}")