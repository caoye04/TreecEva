from itertools import cycle

# Simulate a signal processing pipeline with modular arithmetic
def calculate_phase(value, idx):
    if value % 4 == 0:
        return value + idx
    elif value % 3 == 0:
        return value - idx
    else:
        return value * 2

signal_sequence = [7, 8, 9, 10, 11]
base_mod = 5
index = 3
mod_result = (sum(signal_sequence) + 2) % base_mod

# Extraneous but harmless variable
buffer_size = len(signal_sequence) * 2

phase_shift = calculate_phase(mod_result, index)

# Additional unrelated tracking variable (minor distraction)
cycle_tracker = cycle([1, 0])

print(f"Result: {phase_shift}")