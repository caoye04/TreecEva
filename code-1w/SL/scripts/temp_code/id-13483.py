import math

# Irrelevant helper function (dead code path)
def unused_similarity(a, b):
    return sum(1 for x, y in zip(a, b) if x == y)

# Misleading metric calculation (not actually used in final result)
def compute_legacy_metric(data):
    temp = 0
    for i in range(len(data)):
        temp += (data[i] * (i + 1)) ** 0.5
    return int(temp % 100)

# Decoy weight adjustment with bit manipulation distraction
def adjust_weights_wrongly(w):
    shifted = w << 2
    masked = shifted & 0xFF
    return masked ^ 0xAA

# Core logic: evaluates performance using weighted harmonic mean
def harmonic_weighted_avg(values, w):
    if len(values) != len(w):
        return -1
    weighted_inv_sum = 0.0
    weight_sum = 0.0
    for v, weight in zip(values, w):
        if v != 0:
            weighted_inv_sum += weight / v
            weight_sum += weight
    return weight_sum / weighted_inv_sum if weighted_inv_sum != 0 else 0

# Main evaluation function
def evaluate_performance(m, w):
    # Distractor: initialize unused tracking variables
    snapshot_log = {'peak': 0, 'baseline': None, 'flags': []}
    temp_buffer = [0] * 6
    
    # Irrelevant transformation chain
    transformed = []
    for x in m:
        if x > 50:
            transformed.append(x * 0.9)
        else:
            transformed.append(x * 1.1)
    
    # Another red herring: dictionary-based mapping not used later
    category_map = {
        'A': m[0] * 2,
        'B': m[1] + m[2],
        'C': abs(m[3] - m[4]),
        'D': m[5] >> 1
    }
    
    # Actual relevant computation begins here
    filtered_metrics = [x for x in m if x >= 30]  # Only consider metrics >= 30
    
    # Recompute weights via a non-linear scaling (only this matters)
    adjusted_weights = []
    for idx, wt in enumerate(w):
        scaled = wt * (1 + 0.1 * (idx % 3))
        adjusted_weights.append(round(scaled, 2))
    
    # Apply harmonic mean on filtered data with adjusted weights
    raw_result = harmonic_weighted_avg(filtered_metrics, adjusted_weights[:len(filtered_metrics)])
    
    # Final nonlinear correction based on bit count of integer part
    int_part = int(raw_result)
    parity_offset = bin(int_part).count('1')  # Number of set bits
    final_value = raw_result + (parity_offset * 0.25)
    
    # Critical assignment point
    final_score = int(round(final_value * 2)) / 2  # Round to nearest 0.5
    
    # Redundant logging (no effect)
    debug_info = {}
    for k, v in category_map.items():
        debug_info[k] = f"val={v}, hex={hex(v)}"
    
    return final_score

# Primary execution block
if __name__ == '__main__':
    # Input metrics (performance indicators)
    metrics = [85, 72, 60, 44, 38, 29, 91]
    
    # Base weights for each metric
    weights = [0.8, 1.0, 0.9, 1.1, 0.7, 1.2, 0.6]
    
    # Unused derived arrays (distractors)
    squared_diffs = [(a - b)**2 for a, b in zip(metrics, metrics[1:])]    
    cumulative = []
    total = 0
    for val in metrics:
        total += val
        cumulative.append(total)
    
    # Key statement that produces the answer
    final_score = evaluate_performance(metrics, weights)
    
    # Output result
    print(f"Result: {final_score}")