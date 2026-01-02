from collections import defaultdict, Counter
from itertools import combinations

# Simulate processing of sensor data with noise filtering and pattern detection
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_vals = sorted(filtered)
    
    # Distractor: counting frequencies (not directly used later)
    freq_map = Counter(sorted_vals)
    
    # Extract rising trends of length 3
    trends = []
    for i in range(len(sorted_vals) - 2):
        if sorted_vals[i] < sorted_vals[i+1] < sorted_vals[i+2]:
            trends.append((sorted_vals[i], sorted_vals[i+1], sorted_vals[i+2]))
    
    # Distractor: generate all pairs (unused)
    _ = list(combinations(sorted_vals, 2))
    
    return trends

# Analyze trend stability based on gap consistency
def assess_trend_stability(trends):
    stability_scores = []
    for t in trends:
        diff1 = t[1] - t[0]
        diff2 = t[2] - t[1]
        stability = abs(diff1 - diff2)
        stability_scores.append(10 - min(stability, 10))  # capped score
    
    # Distractor: group by score (semi-relevant but not used directly)
    grouped = defaultdict(list)
    for s in stability_scores:
        grouped[s // 2].append(s)
    
    return sum(stability_scores) if stability_scores else 0

# Recursive helper to compute weighted depth score (used in final calculation)
def compute_depth_score(n):
    if n <= 1:
        return 1
    return n + compute_depth_score(n // 2)

# Core scoring logic
def calculate_final_score(trends):
    base_score = assess_trend_stability(trends)
    adjustment_factor = len(trends) * 0.5
    
    # Distractor: unrelated string processing
    log_tag = "SENSOR_LOG_" + "_".join(map(str, [len(trends), int(adjustment_factor)]))
    parts = log_tag.split('_')
    tag_value = sum(len(p) for p in parts if p.isdigit())
    
    # Actual use of recursive function
    depth_bonus = compute_depth_score(len(trends) + 1)
    
    # Final computation
    raw_final = base_score + adjustment_factor + depth_bonus
    final_score = int(round(raw_final))
    
    return final_score

# Main execution
raw_sensor_data = [5, 15, 20, 25, 30, 8, 35, 40, 12, 45, 55, 60, 110, 50]
processed_data = preprocess_sensor_readings(raw_sensor_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")