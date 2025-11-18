from collections import deque
from functools import reduce

def apply_gain_factor(signal, factor):
    return signal * factor

def is_valid_frequency(freq):
    return freq > 0 and freq <= 20000

def calculate_signal_strength(signals):
    return reduce(lambda x, y: x + y, signals, 0)

# Initialize data structures
frequency_stack = []
data_packets = deque([1.5, 2.0, -0.5, 3.2, 0.8])

# Process data packets with gain factors
gain_factors = [1.2, 0.9, 1.5, 0.7]
gain_applied_signals = list(map(lambda x: apply_gain_factor(x[1], gain_factors[x[0] % len(gain_factors)]), enumerate(data_packets)))

# Apply frequency validation with short-circuit evaluation
valid_signals = list(filter(lambda s: s > 0 and is_valid_frequency(abs(s)*1000), gain_applied_signals))

# Push valid signals to stack (in reverse order)
for signal in reversed(valid_signals):
    frequency_stack.append(signal)

# Calculate processed signal strength
processed_signals = []
while frequency_stack:
    signal = frequency_stack.pop()
    # Only process if signal is above noise threshold
    if signal > 0.5 and (signal * 2.0) > 1.0:
        processed_signals.append(signal)

processed_signal_strength = calculate_signal_strength(processed_signals)
print(f"Result: {processed_signal_strength}")