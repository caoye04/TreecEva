import math
from contextlib import contextmanager

@contextmanager
def precision_tracker(scale):
    try:
        yield lambda x: round(x, scale)
    finally:
        pass

def compute_volatility(base, samples):
    total = 0.0
    with precision_tracker(4) as precise:
        for i in range(len(samples)):
            diff = precise(samples[i] - base)
            total += diff * diff if diff > 0 else -diff * diff
    return total / len(samples) if samples else 0

initial_base = 100.5
sample_values = [98.2, 102.7, 99.8, 105.1, 97.6]
volatility_measure = compute_volatility(initial_base, sample_values)
adjustment_factor = volatility_measure if volatility_measure <= 5.0 else 5.0 if volatility_measure <= 10.0 else 10.0
print(f'Result: {adjustment_factor}')