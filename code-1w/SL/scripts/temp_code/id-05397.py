from itertools import combinations
from functools import reduce

# Simulated sensor data aggregation and performance scoring system
data_stream = [14, 28, 19, 35, 22, 47, 13]
weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.1, 0.0]
thresholds = { 'low': 15, 'high': 30 }

# Irrelevant helper: computes pairwise products (not used in final logic)
def compute_pairwise_products(arr):
    return [a * b for a, b in combinations(arr, 2)]

# Misleading transformation: applies logarithmic scaling to values above threshold
def apply_log_transform(values, base=2.71):
    return [round(v / (base ** 0.5), 3) if v > thresholds['high'] else v for v in values]

# Normalize data using min-max scaling (relevant)
def normalize_values(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Heuristic filter: masks values below noise floor (semi-relevant but bypassed)
mask_noise_floor = lambda arr, floor: [x for x in arr if x >= floor]

# Core evaluation function
def evaluate_performance(weight_vec, norm_data):
    # Step 1: Apply exponential decay to older entries (simulated temporal weighting)
    time_decay = [0.95 ** i for i in range(len(norm_data))]
    weighted_vals = [norm_data[i] * time_decay[i] for i in range(len(norm_data))]
    
    # Step 2: Compute moving average over window size 3 (distractor, not used later)
    moving_avg = []
    for i in range(2, len(weighted_vals)):
        moving_avg.append(sum(weighted_vals[i-2:i+1]) / 3)
    
    # Step 3: Boost values that exceed dynamic threshold
    dynamic_boost = []
    avg_recent = sum(weighted_vals[-3:]) / 3 if len(weighted_vals) >= 3 else weighted_vals[-1]
    for val in weighted_vals:
        if val > avg_recent * 1.1:
            dynamic_boost.append(val * 1.25)
        else:
            dynamic_boost.append(val)
    
    # Step 4: Apply actual metric weights (only this affects final result)
    final_weighted = sum(dynamic_boost[i] * weight_vec[i] for i in range(len(weight_vec)))
    
    # Step 5: Post-processing with clamping
    clamped_score = max(0.0, min(final_weighted, 1.0))
    
    # Step 6: Scale to integer score
    return int(clamped_score * 1000)

# Dead code path: unused alternative scoring
if False:
    def alt_scorer(x):
        return reduce(lambda a, b: a + b, x) % 77

# Execute pipeline
filtered_data = mask_noise_floor(data_stream, thresholds['low'])  # Not actually used
log_corrected = apply_log_transform(data_stream)  # Computed but not used
normalized_data = normalize_values(data_stream)  # This is used
metric_weights = [w * 1.1 for w in weights]  # Adjust weights slightly
metric_weights[-1] = 0.05  # Fix last weight

# Key statement
final_score = evaluate_performance(metric_weights, normalized_data)

print(f"Result: {final_score}")