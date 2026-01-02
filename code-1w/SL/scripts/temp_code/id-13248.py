from itertools import combinations
from functools import reduce

# Simulate sensor data processing with noise filtering and relevance scoring
def preprocess_readings(readings):
    filtered = [x for x in readings if 10 <= x <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Calculate dynamic weight adjustment based on variance
def adjust_weights(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    adjustment = max(0.5, min(1.5, 1 + (variance - 0.1) * 5))
    return [adjustment * 0.8] * 3 + [adjustment * 1.2] * 2

# Misleading auxiliary function - not directly used in final result
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return round(entropy, 4)

# Core evaluation logic
def evaluate_performance(metrics, weights):
    # Apply weighted sum using lambda and zip
    weighted_sum = sum(map(lambda pair: pair[0] * pair[1], zip(metrics, weights)))
    penalty = 0
    
    # Additional logic: check for metric consistency
    for i in range(len(metrics) - 1):
        if metrics[i] > metrics[i+1]:
            penalty += 0.05  # small deduction for non-monotonicity
    
    adjusted = weighted_sum - penalty
    
    # Artificial complexity: generate unused combinatorial features
    combos = list(combinations(metrics, 2))
    combo_products = [a * b for a, b in combos]
    avg_product = sum(combo_products) / len(combo_products) if combo_products else 0
    
    # Dummy tracking state (distractor)
    history = []
    for val in metrics:
        temp = val ** 0.5
        history.append(round(temp, 3))
    
    return int(round(adjusted * 100))

# Raw input data (simulated)
sensor_data = [15, 23, 12, 105, 88, 45, 92, -5, 67, 77, 81]

# Preprocessing stage
processed = preprocess_readings(sensor_data)

# Extract key statistical metrics
mean_proc = sum(processed) / len(processed)
std_dev = (sum((x - mean_proc) ** 2 for x in processed) / len(processed)) ** 0.5
peak = max(processed)
skew = (sum((x - mean_proc) ** 3 for x in processed) / len(processed)) / (std_dev ** 3)
noise_ratio = len([x for x in sensor_data if x < 10 or x > 100]) / len(sensor_data)

metrics = [mean_proc, std_dev, peak, skew, noise_ratio]

# Weight generation (some irrelevant steps included)
base_weights = adjust_weights(processed)
weights = [round(w, 3) for w in base_weights[:5]]  # truncate to match metrics

# Dead code path - never executed but present for distraction
if __debug__:
    debug_info = {"raw_count": len(sensor_data), "filtered": len(processed)}
    redundant_calc = reduce(lambda a, b: a * b, [w + 0.1 for w in weights])

# Key execution point
evaluation_snapshot = metrics[::2]  # slicing for logging (unused)
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")