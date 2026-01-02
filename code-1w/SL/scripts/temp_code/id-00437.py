from collections import defaultdict, Counter
import itertools

# Simulated sensor data with noise and metadata
def load_sensor_data():
    raw = [15, 23, 18, 26, 23, 19, 21, 24, 20, 22]
    meta = {i: {'calibrated': True, 'source': f'Sensor_{i}'} for i in range(len(raw))}
    return list(enumerate(raw)), meta

def analyze_outliers(values):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    threshold = mean + 1.5 * std_dev
    return [v for v in values if v > threshold]

def transform_data(seq, factor=1.1):
    # Irrelevant transformation path
    shifted = [(x * factor) + 2 for x in seq]
    normalized = [x / max(shifted) for x in shifted]
    return [int(x * 100) for x in normalized]

def dummy_aggregate(data_list):
    # Dead function: never used in critical path
    total = 0
    for item in data_list:
        if isinstance(item, dict):
            total += len(item)
    return total

def compute_entropy(arr):
    # Misleading statistical distraction
    counts = Counter(arr)
    total = len(arr)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 4)

def filter_and_weight(pairs, thresholds):
    # Complex filtering with red herrings
    filtered = []
    temp_log = defaultdict(int)
    decoy_sum = 0

    for idx, val in pairs:
        temp_log[idx] += val
        decoy_sum += idx * val
        if val >= thresholds['min_val'] and idx % 2 == 0:
            filtered.append((idx, val))
        elif val < thresholds['min_val']:
            continue

    # Real logic hidden among distractions
    adjusted = [v * 1.5 if i % 3 == 0 else v * 0.8 for i, v in filtered]
    return adjusted

def compute_final_score(data_tuples, weight_map):
    # Core logic buried under abstraction
    ids, vals = zip(*data_tuples)
    
    # Distractor: unused intermediate stats
    avg_id = sum(ids) / len(ids)
    mode_val = Counter(vals).most_common(1)[0][1]
    
    # Real computation begins
    thresh = {'min_val': 19}
    processed = filter_and_weight(data_tuples, thresh)
    
    # Weight application
    score = 0
    for i, val in enumerate(processcessed):
        weight = weight_map.get(i, 0.9)
        score += val * weight
        if score > 100:
            score -= 10  # artificial cap mechanic
    
    # Final nonlinear adjustment
    penalty = len([x for x in vals if x < 20]) * 1.5
    score = (score - penalty) * 1.1
    
    # Critical result
    final_score = int(round(score))
    return final_score

# --- Main Execution ---
sensor_data, metadata = load_sensor_data()

# Irrelevant preprocessing branch
dummy_stats = []
for _ in range(3):
    dummy_stats.append(transform_data([x[1] for x in sensor_data]))

# Real data flow
cleaned_pairs = [(i, v) for i, v in sensor_data if v > 14]  # redundant filter

# Weight configuration (some entries are decoys)
weights = {
    0: 1.2,
    1: 0.8,
    2: 1.0,
    3: 1.5,  # unused due to filtering
    4: 0.7   # unused
}

# Compute final score
final_score = compute_final_score(cleaned_pairs, weights)

# Output result
print(f"Result: {final_score}")