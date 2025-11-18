from collections import deque
from statistics import mean, variance
class SignalNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def build_signal_chain(values):
    if not values:
        return None
    head = SignalNode(values[0])
    current = head
    for val in values[1:]:
        current.next = SignalNode(val)
        current = current.next
    return head

def compute_variance_of_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return variance(values) if len(values) > 1 else 0

def apply_bitwise_mask(head, mask):
    current = head
    while current:
        current.value &= mask
        current = current.next

signal_data = [12, 28, 35, 42, 56, 63]
signal_chain = build_signal_chain(signal_data)
mask = 0b111100  # 60 in decimal
apply_bitwise_mask(signal_chain, mask)
variance_result = compute_variance_of_linked_list(signal_chain)
values_for_mean = []
current = signal_chain
while current:
    values_for_mean.append(current.value)
    current = current.next
mean_value = mean(values_for_mean)
processed_signal_strength = int(mean_value + variance_result) ^ (mask >> 2)
print(f"Result: {processed_signal_strength}")