from collections import namedtuple
from math import sqrt

class Node:
    def __init__(self, id, signal_strength):
        self.id = id
        self.signal_strength = signal_strength
        self.next = None
    
def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def calculate_attenuation_factor(position, fib_val):
    golden_ratio = (1 + sqrt(5)) / 2
    adjustment = (position * 0.739) % 1.0
    return (fib_val * golden_ratio) + adjustment

# Create linked list of network segments
head = Node('SEG_A', 98.5)
node_b = Node('SEG_B', 92.3)
node_c = Node('SEG_C', 87.1)
node_d = Node('SEG_D', 76.8)
node_e = Node('SEG_E', 65.4)

head.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e

# Valid segment identifiers
valid_segments = frozenset(['SEG_A', 'SEG_C', 'SEG_E'])
processed_segments = set()

# Process network segments
attenuation_values = []
fib_sequence = generate_fibonacci_sequence(10)
position_counter = 1

current_node = head
while current_node:
    if current_node.id in valid_segments:
        processed_segments.add(current_node.id)
        fib_index = (position_counter - 1) % len(fib_sequence)
        attenuation = calculate_attenuation_factor(position_counter, fib_sequence[fib_index])
        adjusted_attenuation = attenuation - (current_node.signal_strength * 0.01)
        attenuation_values.append(adjusted_attenuation)
    position_counter += 1
    current_node = current_node.next

# Calculate final attenuation
final_attenuation = 0.0
for i, val in enumerate(attenuation_values):
    weight = (i + 1) * 0.5
    final_attenuation += val * weight

final_attenuation = round(final_attenuation, 6)
print(f"Result: {final_attenuation}")