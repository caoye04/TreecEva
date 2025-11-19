from functools import reduce
from collections import defaultdict

class SignalNode:
    def __init__(self, freq_coeff=0, next_node=None):
        self.freq_coeff = freq_coeff
        self.next = next_node

def build_signal_chain(coeff_list):
    if not coeff_list:
        return None
    head = SignalNode(coeff_list[0])
    current = head
    for coeff in coeff_list[1:]:
        current.next = SignalNode(coeff)
        current = current.next
    return head

def traverse_and_transform(signal_head, transform_func):
    values = []
    current = signal_head
    while current and current.freq_coeff != 0:
        values.append(transform_func(current.freq_coeff))
        current = current.next
    return values

def selective_filter(x):
    return x if x > 0 and x % 2 == 0 else 0

# Initialize signal processing chain
raw_coefficients = [4, -3, 8, 0, 15, -6, 2]
signal_chain = build_signal_chain(raw_coefficients)

# Apply transformation pipeline
transformed_values = traverse_and_transform(signal_chain, selective_filter)
filtered_map = map(lambda x: x * 2 if x and x < 10 else x, transformed_values)
reduction_result = reduce(lambda acc, val: acc + val if val and acc < 20 else acc, filtered_map, 0)

# Short-circuit evaluation with defaultdict for error handling
cache = defaultdict(int)
validation_passed = reduction_result > 0 and cache['checksum'] == 0
final_output = reduction_result * 2 if validation_passed else -1

print(f"Result: {final_output}")