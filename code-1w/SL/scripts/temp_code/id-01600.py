import itertools

# Sensor simulation parameters (distractor: not all are used)
sampling_rate = 44100
window_size = 1024
overlap_ratio = 0.5
baseline_threshold = 0.7
noise_floor = 0.001

# Raw sensor inputs (simulated)
raw_readings = [0.1, 0.8, 1.2, 0.9, 0.4, 1.6, 1.8, 0.2, 0.7, 1.1]

def preprocess(signal_list):
    # Irrelevant normalization path (dead code in practice due to later override)
    normalized = [x / max(signal_list) for x in signal_list]
    filtered = list(filter(lambda x: x > baseline_threshold, normalized))
    return filtered

# Misleading transformation chain
shadow_copy = [x * 1.5 for x in raw_readings if x > 0.5]
decoy_moment = sum([x ** 2 for x in shadow_copy]) / len(shadow_copy)

# Actual preprocessing step (overwrites prior logic)
processed_signals = []
for val in raw_readings:
    if val > 0.6:
        processed_signals.append(val * 2)
    elif val < 0.3:
        processed_signals.append(val * 0.5)
    else:
        processed_signals.append(val)

# Unused diagnostic function (decoy)
def compute_entropy(data):
    from math import log
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * log(p) for p in probs if p > 0)

# Real analysis begins
aggregated = 0
for window in itertools.pairwise(processed_signals):
    diff = abs(window[1] - window[0])
    if diff > 0.5:
        aggregated += diff * 10
    else:
        aggregated += diff

# Secondary transformation using lambda and list comprehension
intensities = [(lambda x: x ** 2 + 0.1)(x) for x in processed_signals if x > 1.0]
peak_count = len(intensities)

# Distractor: unused combinatorics
combinations = list(itertools.combinations([1, 2, 3, 4], 2))
combination_sum = sum(a * b for a, b in combinations)  # Never used

# Core diagnostic logic
status_flags = {"stable": 0, "warning": 0, "alert": 0}

for x in processed_signals:
    if x > 1.5:
        status_flags["alert"] += 1
    elif x > 0.8:
        status_flags["warning"] += 1
    else:
        status_flags["stable"] += 1

# Critical intermediate with misleading name
pseudo_entropy = (status_flags["alert"] * 2.1) + (status_flags["warning"] * 0.7)

# Final analysis incorporating multiple concepts
def analyze_readings(data):
    base_score = sum(x for x in data if x > 1.0)
    penalty = len([x for x in data if x < 0.3]) * 0.5
    adjustment = 0
    
    # Nested condition with red herring variables
    temp_accum = 0
    for i, val in enumerate(data):
        if i % 2 == 0 and val > 0.5:
            temp_accum += val
        # Distractor loop with no effect on output
        for j in range(2):  
            _ = (i + j) % 3  
    
    if temp_accum > 3.0:
        adjustment = 1.2
    
    return int(base_score - penalty + adjustment)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output requirement
print(f"Result: {final_diagnostic}")