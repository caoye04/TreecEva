from functools import reduce

def state_machine_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

class StateProcessor:
    def __init__(self, initial_state):
        self.state = initial_state
        self.transitions = {
            0: lambda x: (x >> 1) & 3,
            1: lambda x: (x ^ 0xF) & 3,
            2: lambda x: (x << 1) & 3,
            3: lambda x: (x | 0x3) & 3
        }
    
    def process_chunk(self, chunk):
        next_state_op = self.transitions[self.state]
        self.state = next_state_op(chunk)
        return self.state

# Control value determines initial state
control_value = 42
initial_state = control_value & 1  # Even -> state 0, Odd -> state 1

# Initialize processor
processor = StateProcessor(initial_state)

# Data chunks to process
data_chunks = [0x5, 0xA, 0x3, 0xF, 0x7]

# Process each chunk
state_history = [initial_state]
for chunk in data_chunks:
    current_state = processor.process_chunk(chunk)
    state_history.append(current_state)

# Calculate final checksum using floating point ops
checksum_components = list(map(lambda s, i: (s + 1) * (i + 1.5), state_history, range(len(state_history))))
intermediate_sum = reduce(lambda acc, val: acc + val, checksum_components, 0.0)
final_checksum = intermediate_sum / len(checksum_components)

print(f"Result: {final_checksum}")