def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    count = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def smooth_data(values):
    smoothed = [values[0]]
    for i in range(1, len(values)-1):
        smoothed.append((values[i-1] + values[i] + values[i+1]) // 3)
    smoothed.append(values[-1])
    return smoothed

# Unused transformation function (dead code path)
def transform_scale(arr, factor=2):
    return [x * factor for x in arr]

# Distractor: complex but unused bitwise logic
def flag_computation(x, y):
    temp = (x ^ y) & 0xFF
    temp = (temp << 3) | (temp >> 5)
    return temp % 97

# Main data processing chain
def extract_features(dataset):
    features = {}
    for idx, row in enumerate(dataset):
        features[idx] = {
            'sum': sum(row),
            'max': max(row),
            'min': min(row),
            'range': max(row) - min(row)
        }
    return features

def compute_weighted_sum(values, w):
    return sum(v * w[i % len(w)] for i, v in enumerate(values))

# Core logic buried among distractions
def validate_sequence(arr):
    if not arr:
        return False
    sorted_check = arr == sorted(arr)
    unique_check = len(set(arr)) == len(arr)
    return sorted_check and unique_check

# Critical function with distractors
weights = [0.1, 0.3, 0.4, 0.2]
data = [
    [12, 15, 10, 8],
    [7,  9,  13, 11],
    [6,  5,  8,  9],
    [4,  7,  6,  5]
]

feature_map = extract_features(data)

# Misleading intermediate computation (not used in final result)
phantom_score = 0
for k, v in feature_map.items():
    phantom_score += v['range'] * (k + 1)

# Another red herring: complex enumeration with zip
offsets = [2, -1, 3, 0]
eval_pairs = []
for i, (row, offset) in enumerate(zip(data, offsets)):
    adjusted = [(val + offset) ** 2 for val in row]
    eval_pairs.append((i, sum(adjusted)))

# Real computation hidden here
aggregated = []
for i in range(len(data)):
    feat = feature_map[i]
    raw_vals = data[i]
    # Only this line contributes to final answer
    metric = (feat['sum'] * 0.5) + (feat['max'] * 0.3) - (feat['min'] * 0.2)
    aggregated.append(metric)

# Final processing with tuple unpacking distraction
temp_results = []
for idx, val in enumerate(aggregated):
    temp_results.append((idx, val, val ** 0.5))

# Unpacking that looks important but only uses one component
decoy_total = 0
for _, score, _ in temp_results:
    decoy_total += int(score)

# Key statement - answer depends on this
final_score = process_metrics(data, weights)

# Actual definition of process_metrics (buried late)
def process_metrics(dataset, weight_vector):
    totals = [sum(row) for row in dataset]
    weighted = compute_weighted_sum(totals, weight_vector)
    adjustment = analyze_pattern(totals)
    return int(weighted) + adjustment * 10

# Print result as required
Result: {final_score}