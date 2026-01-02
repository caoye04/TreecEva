import itertools

def analyze_sequence(pattern, threshold):
    count = 0
    for i in range(len(pattern)):
        if sum(pattern[:i+1]) > threshold:
            count += 1
    return count

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    total = len(data)
    for f in freq.values():
        p = f / total
        entropy -= p * log(p, 2)
    return entropy

# Misleading intermediate processing
temp_readings = [23.5, 24.1, 22.8, 25.6, 26.0, 24.3]
adjusted_readings = [x + 0.5 for x in temp_readings if x < 25]  # Partial filtering (distractor)

# Unused but plausible transformation
cumulative_shift = list(itertools.accumulate([1, -1, 2, -2, 3], lambda acc, x: acc + x if acc % 2 == 0 else acc - x))

# Simulated sensor data with noise (mostly irrelevant)
sensor_grid = [[i*j + 0.1 for j in range(1, 5)] for i in range(1, 6)]
valid_sensors = [any(x > 10 for x in row) for row in sensor_grid]
active_count = sum(valid_sensors)

# Core logic disguised among distractions
def normalize_vector(v):
    magnitude = sum(x**2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

def recursive_filter(items, depth=0):
    if depth >= 3 or len(items) <= 1:
        return items[0] if items else 0
    mid = len(items) // 2
    left = recursive_filter(items[:mid], depth + 1)
    right = recursive_filter(items[mid:], depth + 1)
    return abs(left - right)

# Real data chain
raw_metrics = [88, 92, 76, 95, 85]
weight_template = [3, 2, 1, 4, 2]

# Distracting normalization variant (unused)
min_max_norm = lambda x: (x - min(raw_metrics)) / (max(raw_metrics) - min(raw_metrics)) if max(raw_metrics) != min(raw_metrics) else 0

# Actual preprocessing
scaled_metrics = [x / 10 for x in raw_metrics]  # Step 1: scale down
offset_correction = sum(scaled_metrics) / len(scaled_metrics)  # Step 2: baseline
aligned_metrics = [x - offset_correction + 5 for x in scaled_metrics]  # Step 3: center around 5

# Weight manipulation with red herring
potential_weights = list(itertools.permutations(weight_template[:3]))  # unused complex structure
metric_weights = normalize_vector(weight_template)  # actual weights used

# More misdirection: unused conditional path
if len(potential_weights) > 10:
    metric_weights = [w * 1.1 for w in metric_weights]

# Data slicing that looks important but isn't fully used
segment_a = aligned_metrics[1:4]
segment_b = aligned_metrics[::-2]  # reverse every other

# Normalized data preparation (key step)
normalized_data = [round(aligned_metrics[i] * metric_weights[i], 4) for i in range(len(aligned_metrics))]

# Another decoy function call
dummy_analysis = analyze_sequence([1, 2, -1, 3, -2], 3)

# Critical computation hidden in generic name
def evaluate_performance(weights, data):
    score = 0
    for i in range(len(data)):
        score += weights[i] * data[i] * 1.5  # weighted accumulation
    # Additional logic to obscure the path
    if score > 100:
        score *= 0.95
    else:
        score += 10
    # Final adjustment based on pattern
    trend = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    if trend >= 3:
        score += 5
    return int(round(score))

# Execution point of interest
final_score = evaluate_performance(metric_weights, normalized_data)
print(f"Result: {final_score}")