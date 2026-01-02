def analyze_phase_transition(data, limit):
    temp = 0
    for i in range(len(data)):
        if data[i] > limit:
            temp += (data[i] ** 0.5) // 1
    return int(temp)

# Irrelevant helper function (dead code path)
def compute_entropy(arr):
    entropy = 0.0
    for x in arr:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Misleading intermediate calculation
efficiency_ratio = 0.0
baseline = [1, 2, 3, 4, 5]
offset = sum([x ** 2 for x in baseline])  # Red herring: not used later

# Another decoy function with unused logic
def evaluate_stability(seq):
    total = 0
    for item in seq:
        total += item << 2
    return total % 7 == 0  # Never called

import math

# Core data structures with distractors
event_log = [16, 9, 25, 36, 49, 64]
buffer_cache = [x + 1 for x in event_log]  # Unused distraction

scaling_factor = 2.5
adjustment = 1.2  # Looks important but irrelevant

# Conditional expression used idiomatically
dynamic_flag = True if len(event_log) > 5 else False

# Key preprocessing step disguised among noise
filtered_data = [x for x in event_log if math.sqrt(x) % 1 == 0]

# Secondary filtering that looks significant but is redundant
cleaned_data = []
for val in filtered_data:
    if val >= 25:
        cleaned_data.append(val)

# Threshold computed via complex-looking but straightforward logic
threshold = sum([int(math.sqrt(x)) for x in cleaned_data]) // len(cleaned_data)

# Energy profile derived from root-transformed values
energy_profile = [int(math.sqrt(x)) * scaling_factor for x in event_log]

# Real computation buried in abstraction
def measure_efficiency(signal, t):
    accumulated = 0
    count = 0
    for level in signal:
        # Simulate conditional amplification
        boost = 1.5 if level > t else 1.0
        adjusted_level = level * boost
        accumulated += adjusted_level
        count += 1
    # Final transformation using conditional expression
    average = accumulated / count
    return int(average) if dynamic_flag else round(average, 2)

# Critical statement
thermal_capacity = measure_efficiency(energy_profile, threshold)

# Print result as required
print(f"Result: {thermal_capacity}")