import itertools

# Simulated sensor fusion system for environmental monitoring

def collect_readings():
    # Real data source (relevant)
    base_readings = [12.5, 18.3, 9.7, 22.1, 14.6]
    adjustments = [0.8, -1.2, 0.5, -0.3, 1.1]
    adjusted = [base_readings[i] + adjustments[i] for i in range(len(base_readings))]
    return adjusted

# Irrelevant helper - looks useful but unused in final path
def smooth_data(data, passes=2):
    temp = data.copy()
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[(i+1) % len(temp)]) / 3 for i in range(len(temp))]
    return temp

# Decoy function that processes unrelated metrics
def calculate_stability_index(stream):
    if len(stream) < 2:
        return 0.0
    diffs = [abs(stream[i] - stream[i-1]) for i in range(1, len(stream))]
    return sum(diffs) / len(diffs) * 100  # Larger number for distraction

# Core transformation chain (relevant)
def normalize_readings(raw):
    min_val, max_val = min(raw), max(raw)
    if max_val == min_val:
        return [0.5 for _ in raw]
    return [(x - min_val) / (max_val - min_val) for x in raw]

# Weighted aggregation with conditional boosting

def apply_boost(metrics, thresholds):
    boosted = []
    for i, val in enumerate(metrics):
        if val > thresholds[i]:
            val = val * 1.25  # Boost high performers
        boosted.append(min(val, 1.0))  # Cap at 1.0
    return boosted

def compute_entropy(weights):
    # Looks complex but irrelevant to final score
    import math
    total = 0.0
    for w in weights:
        if w > 0:
            total -= w * math.log(w)
    return round(total, 6)

# Main evaluation logic (key path)

def evaluate_performance(weights, results):
    # Step 1: Normalize raw results
    normalized = normalize_readings(results)
    
    # Step 2: Apply conditional boosts based on threshold criteria
    thresholds = [0.4, 0.5, 0.3, 0.6, 0.5]
    enhanced = apply_boost(normalized, thresholds)
    
    # Step 3: Compute weighted sum (actual answer path)
    weighted_sum = sum(enhanced[i] * weights[i] for i in range(len(weights)))
    
    # Step 4: Apply scaling factor derived from bit manipulation (red herring below)
    scale_factor = 1.0
    debug_flag = 0b101010
    config_mask = 0b110000
    mode_bits = debug_flag & config_mask
    if mode_bits >> 4:
        scale_factor = 0.9  # Unused path - misleading
    
    # Step 5: Additional adjustment using itertools cycle (distractor computation)
    pattern = [0.98, 1.02, 0.99]
    multiplier_cycle = itertools.cycle(pattern)
    adjustment = 1.0
    for _ in range(len(results)):
        adjustment *= next(multiplier_cycle)  # Cancels out due to symmetry
    
    # Final computation - only weighted_sum matters; others are distractors
    raw_final = weighted_sum * 100  # Scale to integer-friendly range
    
    # Dead code path - never executed but looks important
    def audit_trail(data):
        return [round(x, 3) for x in data if x > 0.1]
    
    # Return final performance score as integer
    return int(round(raw_final))

# Global configuration (mix of relevant and irrelevant)
metric_weights = [0.2, 0.3, 0.1, 0.25, 0.15]  # Sum = 1.0
raw_results = collect_readings()  # [13.3, 17.1, 10.2, 21.8, 15.7]

# Phantom data structures - not used
decoy_dataset = list(itertools.permutations([1, 2, 3], 3))
auxiliary_map = {k: v for k, v in enumerate(itertools.accumulate([1, 2, 1, 3]))}

# Key execution point
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")