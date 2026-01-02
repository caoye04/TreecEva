def analyze_pattern(sequence):
    """Irrelevant analysis function - distractor"""
    if len(sequence) < 5:
        return False
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i+1]:
            count += 1
    return count > 2

# Irrelevant constants - red herring
MAX_BUFFER_SIZE = 1024
DEBUG_MODE = True
DEFAULT_TIMEOUT = 30

# Real data
raw_inputs = [18, 22, 35, 41, 28, 33, 39, 26]
offsets = [3, -5, 2, -1, 4, -3, 1, -2]
weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.85, 0.95, 1.15]

# Distractor: unused function
def normalize(data):
    m = sum(data) / len(data)
    return [(x - m) * 0.5 for x in data]

# Distractor: misleading intermediate calculation
aggregate_total = sum([x * 1.05 for x in raw_inputs if x > 30])

# Key transformation chain begins
adjusted = [raw_inputs[i] + offsets[i] for i in range(len(raw_inputs))]
scaled_values = [round(adjusted[i] * weights[i], 4) for i in range(len(adjusted))]

# Decoy list processing
filtered_outliers = [x for x in scaled_values if 25 < x < 45]

# Unused conditional block - dead code path
if DEBUG_MODE:
    temp_checksum = 0
    for idx, val in enumerate(scaled_values):
        temp_checksum ^= int(val)

# Another irrelevant computation
simulated_cache = {i: (i ** 2) % 7 for i in range(1, 9)}

# Threshold logic with slicing distraction
activation_window = scaled_values[2:6]
thresholds = [32.5, 38.0, 30.0, 40.5]

# Conditional expression mix
penalties = [1.5 if val > thr else 0.5 for val, thr in zip(activation_window, thresholds)]
bonus_flag = any(val > 40 for val in activation_window)

# Core logic hidden among distractions
def compute_aggregate(values, limits):
    base = sum(values[:len(limits)])
    adjustment = 0
    for v, t in zip(values, limits):
        if v >= t:
            adjustment += (v - t) * 0.7
        else:
            adjustment -= (t - v) * 0.3
    # Final non-linear boost
    multiplier = 1.1 if bonus_flag else 0.9
    return round((base + adjustment) * multiplier, 4)

# Critical statement
final_score = compute_aggregate(scaled_values, thresholds)

# Distractor: redundant enumeration
status_map = {}
for index, value in enumerate(scaled_values):
    status_map[f'node_{index}'] = 'active' if value > 30 else 'idle'

# Print required output
print(f"Result: {final_score}")