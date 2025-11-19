class SignalNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def process_signal_chain(chain_head, transform_map):
    current = chain_head
    accumulator = 0
    while current:
        if current.value in transform_map:
            transformed = transform_map[current.value]
            if transformed & 1:
                accumulator ^= (current.value << 1) % 17
            else:
                accumulator = (accumulator + transformed) & 0xFF
        else:
            accumulator = (accumulator * 3) % 13
        current = current.next
    return accumulator

def build_signal_chain(values):
    if not values:
        return None
    head = SignalNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SignalNode(val)
        current = current.next
    return head

# Initialize transformation lookup table
transform_lookup = {
    5: 12,
    10: 7,
    3: 15,
    8: 2,
    12: 9
}

# Create signal chain
signal_values = [5, 10, 3, 8, 12, 1, 7]
signal_chain = build_signal_chain(signal_values)

# Process the signal chain
intermediate_result = process_signal_chain(signal_chain, transform_lookup)

# Apply final transformation
final_signal_strength = 0
for i in range(4):
    mask = (intermediate_result >> (i * 2)) & 0x3
    if mask == 0:
        final_signal_strength += 1 << i
    elif mask & 0x1:
        final_signal_strength ^= (mask << (i + 1))
    else:
        final_signal_strength &= ~(mask >> 1)

# Apply modular correction
final_signal_strength = (final_signal_strength ^ 0xF) % 11
print(f"Result: {final_signal_strength}")