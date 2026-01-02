from collections import defaultdict
from itertools import combinations

# Simulated sensor data processing for environmental monitoring system
def collect_readings():
    raw_data = [105, 210, 190, 205, 180, 215, 170]
    offset = 50
    adjusted = [x - offset for x in raw_data]
    return adjusted

# Filter out anomalous spikes using simple threshold logic
def filter_anomalies(readings, limit=150):
    normal = []
    spike_count = 0
    temp_buffer = []  # unused buffer (distractor)

    for val in readings:
        if val > limit:
            spike_count += 1
        else:
            normal.append(val)
    
    # Irrelevant transformation (distractor)
    scaled = [x * 1.1 for x in normal if x > 100]
    return normal

# Compute stability metrics across valid segments
def compute_stability(sequence):
    diffs = []
    for i in range(1, len(sequence)):
        diffs.append(abs(sequence[i] - sequence[i-1]))
    
    avg_fluctuation = sum(diffs) / len(diffs) if diffs else 0
    max_jump = max(diffs) if diffs else 0
    
    # Extra computation not used later (distractor)
    trend_consistency = sum(1 for d in diffs if d < avg_fluctuation)
    
    return {'avg_change': avg_fluctuation, 'peak_variation': max_jump}

# Evaluate overall performance based on multiple metrics
def evaluate_performance(metrics, config):
    base = metrics['avg_change']
    penalty = 0
    
    if metrics['peak_variation'] > config['variation_cap']:
        penalty += config['penalty_high_var']
    
    # Secondary check with distractor logic
    adjustment_factor = 0.9
    dummy_tracker = defaultdict(int)
    for k in metrics:
        dummy_tracker[k] += 1  # no effect on result
    
    # Additional red herring: combination analysis (unused)
    pairs = list(combinations(metrics.values(), 2))
    pair_sum = sum(a + b for a, b in pairs) if pairs else 0
    
    # Core scoring logic
    raw_score = base * 10
    final_score = int(raw_score - penalty)
    
    # Dead code path (distractor)
    if False:
        fallback = sum(dummy_tracker.values())
        final_score = fallback
        
    return final_score

# Main execution flow
if __name__ == '__main__':
    readings = collect_readings()
    clean_data = filter_anomalies(readings)
    metric_data = compute_stability(clean_data)
    
    # Threshold configuration (some values are unused)
    thresholds = {
        'variation_cap': 25,
        'penalty_high_var': 15,
        'baseline_floor': 5  # unused parameter
    }
    
    final_score = evaluate_performance(metric_data, thresholds)
    print(f"Result: {final_score}")