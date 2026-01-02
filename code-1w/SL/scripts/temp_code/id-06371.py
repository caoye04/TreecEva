import math

def calculate_weighted_sum(values, weights):
    weighted_sum = 0.0
    for i, (val, w) in enumerate(zip(values, weights)):
        phase_shift = math.sin(val)
        weighted_sum += phase_shift * w
    return weighted_sum

def analyze_signal_integrity(signal_data):
    base_correction = 0.5
    return base_correction  # Irrelevant to final result, minor distraction

# Simulate harmonic phase analysis
phases = [math.pi / 6, math.pi / 4, math.pi / 3]
weights = [2, 3, 4]

# Key computation
intermediate_check = sum(phases)  # Distractor: used for no critical path
total_harmony = calculate_weighted_sum(phases, weights)

# Output result
print(f"Result: {total_harmony}")