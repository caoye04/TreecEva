from collections import deque
from functools import reduce

def apply_modulation(freq, mod):
    return (freq * 2 + mod) & 0xFF

class SignalProcessor:
    def __init__(self):
        self.adjustments = deque()
    
    def push_adjustment(self, val):
        self.adjustments.append(val)
    
    def pop_adjustment(self):
        return self.adjustments.pop() if self.adjustments else 0

modulations = [3, 7, -2, 11]
frequency_stack = [15, 22, 8, 31]
signal_proc = SignalProcessor()

for m in modulations:
    signal_proc.push_adjustment(m)

base_freq = 100
processed_signal_strength = 0

while frequency_stack:
    current_freq = frequency_stack.pop()
    if current_freq > 20:
        adjustment = signal_proc.pop_adjustment()
        modulated = apply_modulation(current_freq, adjustment)
        processed_signal_strength += modulated
        if modulated < 50:
            break
    else:
        processed_signal_strength -= current_freq

signal_map = {i: v for i, v in enumerate([10, 20, 30, 40])}
adjusted_map = {k: v + processed_signal_strength for k, v in signal_map.items()}
final_values = list(adjusted_map.values())
processed_signal_strength = reduce(lambda x, y: x ^ y, final_values)

print(f"Result: {processed_signal_strength}")