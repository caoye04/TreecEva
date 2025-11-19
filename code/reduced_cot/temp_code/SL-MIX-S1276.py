from functools import reduce

class SensorNode:
    def __init__(self, amplitude, next_node=None):
        self.amplitude = amplitude
        self.next = next_node

# Initialize sensor data as a linked list
head = SensorNode(15)
head.next = SensorNode(9)
head.next.next = SensorNode(22)
head.next.next.next = SensorNode(7)
head.next.next.next.next = SensorNode(31)

# Transformation pipeline
transform = lambda x: (x & 0xF) if x > 10 else (x | 0x10)
filter_valid = lambda x: x != 0
normalize = lambda x: x >> 1 if x & 1 == 0 else (x << 1)

# Process signal through pipeline
node = head
accumulated = 0
while node:
    raw_value = node.amplitude
    transformed = transform(raw_value)
    normalized = normalize(transformed) if filter_valid(transformed) else 0
    accumulated += normalized
    node = node.next

# Final adjustment using ternary and reduction
adjustment_factor = 2 if accumulated % 3 == 0 else (1 if accumulated % 3 == 1 else -1)
values = []
node = head
while node:
    val = transform(node.amplitude)
    values.append(val if val > 5 else val * adjustment_factor)
    node = node.next

processed_signal = reduce(lambda acc, v: acc + (v ^ 0xFF) if v & 0x8 else acc + v, values, 0)
print(f"Result: {processed_signal}")