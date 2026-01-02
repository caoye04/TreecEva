def analyze_trends(data, threshold):
    trend_data = []
    for i, value in enumerate(data):
        if value > threshold:
            trend_data.append((i, value * 1.1))
        elif value == threshold:
            trend_data.append((i, value * 0.95))
        else:
            trend_data.append((i, value * 0.8))
    return trend_data

# Irrelevant helper function (decoy)
def normalize_values(arr):
    max_val = max(arr) if arr else 1
    return [x / max_val for x in arr]

# Unused complex transformation (dead code path)
def transform_metrics(met):
    return {k: v ** 2 for k, v in met.items() if v > 0}

# Distractor variables
temp_offset = 3.14159
scaling_factor = 1.61803
buffer_zone = set([1, 2, 3, 5, 8, 13])
shadow_copy = [x * 2 for x in range(10)]

# Real data used in computation
baseline = {'alpha': 5, 'beta': 8, 'gamma': 3}
metrics = {'alpha': 7, 'beta': 6, 'gamma': 4, 'delta': 2}  # delta is ignored

# Simulated sensor readings (irrelevant)
sensor_log = [
    {'time': 0, 'reading': 100},
    {'time': 1, 'reading': 102},
    {'time': 2, 'reading': 98}
]

# Bit manipulation red herring
bitmask = 0b101010
masked_data = bitmask & 0b111100
shifted_mask = masked_data >> 2

# Set operations with distractors
disjoint_set = {10, 20, 30}
overlap_set = {5, 8, 10}
intersection_clue = disjoint_set & overlap_set  # {10}, irrelevant

# Zip usage (partially relevant)
weights = [0.4, 0.35, 0.25]
eval_keys = ['alpha', 'beta', 'gamma']
key_weight_map = dict(zip(eval_keys, weights))

# Secondary distraction: unused nested loop
accumulator = 0
for x in range(3):
    for y in range(3):
        accumulator += x * y

# Core logic buried within distractions
def evaluate_performance(met, base):
    score = 0
    deviations = []
    
    for key, base_val in base.items():
        actual = met.get(key, 0)
        deviation = abs(actual - base_val)
        deviations.append(deviation)
        if actual >= base_val:
            score += 10
        else:
            score += 5
    
    # Use of enumerate in meaningful context
    for idx, dev in enumerate(deviations):
        if idx % 2 == 0:
            score += dev * 2
        else:
            score += dev

    # Final adjustment using bit operation (light relevance)
    if score & 1:  # if odd
        score += 11
    else:
        score += 7

    return score

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print required output
print(f"Result: {final_score}")