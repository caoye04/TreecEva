from functools import reduce
import itertools

def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def apply_fibonacci_filter(signals):
    fib_weights = list(fibonacci_sequence(len(signals)))
    weighted_signals = [s * w for s, w in zip(signals, fib_weights)]
    return reduce(lambda x, y: x + y, weighted_signals)

def normalize_signal(signal_value, normalization_factor=10):
    return signal_value / normalization_factor if normalization_factor != 0 else 0

# Deep space signal measurements (arbitrary units)
space_signals = [5, 8, 13, 21, 34]

# Apply transformation process
weighted_sum = apply_fibonacci_filter(space_signals)
filtered_signal_strength = normalize_signal(weighted_sum)

# Additional processing step
if filtered_signal_strength > 10:
    adjustment_factor = len(list(itertools.combinations(range(3), 2)))
    filtered_signal_strength += adjustment_factor
else:
    adjustment_factor = len(set(space_signals)) - len(frozenset(space_signals))
    filtered_signal_strength -= adjustment_factor

print(f"Result: {filtered_signal_strength}")