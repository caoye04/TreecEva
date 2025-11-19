from functools import reduce

def modulated_fibonacci(n, phase_set):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        next_val = a + b
        phase_factor = len(phase_set.intersection(set(range(next_val % 10))))
        adjusted_val = next_val - phase_factor if next_val > phase_factor else next_val + phase_factor
        a, b = b, adjusted_val
    return b

signal_phases = frozenset([1, 3, 5, 7, 9])
modulation_func = lambda x: x * 2 if x % 2 == 0 else x // 2
harmonic_index = 8
base_frequency = 3
adjusted_harmonic = harmonic_index if harmonic_index > base_frequency else base_frequency
phase_shifted_signal = modulated_fibonacci(adjusted_harmonic, signal_phases)
processed_signal_strength = modulation_func(phase_shifted_signal) + (10 if phase_shifted_signal % 3 == 0 else 5)
print(f"Result: {processed_signal_strength}")