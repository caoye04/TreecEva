from itertools import cycle
import math

def calculate_phase(signal, freq):
    total = 0
    for i, amplitude in enumerate(signal):
        angle = amplitude * math.sin(2 * math.pi * freq * (i / len(signal)))
        total += angle
    return round(total, 3)

# System parameters
time_steps = 16
base_frequency = 3.5
amplitude_profile = [1, 3, 2, 0, 4, 1, 2, 3]

# Generate oscillation signal using modular indexing with itertools
doubled_profile = amplitude_profile * 2
oscillations = [doubled_profile[i] for i in range(0, time_steps, 2)]

# Superfluous variable - mild distraction (low interference)
temp_scaling = [x * 1.5 for x in amplitude_profile]

# Core computation
harmonic_phase = calculate_phase(oscillations, base_frequency)

# Output result as required
print(f"Result: {harmonic_phase}")