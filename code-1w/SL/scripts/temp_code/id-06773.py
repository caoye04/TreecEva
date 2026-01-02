from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [120, 85, 90, 110, 95, 100, 130]
    timestamps = list(range(len(raw_data)))
    
    # Misleading data aggregation
    temp_aggr = defaultdict(int)
    for i, val in enumerate(raw_data):
        temp_aggr[f'bin_{i % 3}'] += val // 10
    
    processed = []
    for val in raw_data:
        if val > 90:
            processed.append(val + 5)
        else:
            processed.append(val - 3)
    
    # Distractor transformation
    transformed = [x * 1.05 for x in raw_data if x > 80]
    avg_transformed = sum(transformed) / len(transformed) if transformed else 0
    
    # Actual return value used later
    return {'readings': processed, 'count': len(processed)}

# Baseline calibration with red herring calculations
def calibrate_system(mode='standard'):
    base_config = {'threshold': 92, 'hysteresis': 8}
    
    # Irrelevant mode logic (not actually used)
    if mode == 'boosted':
        base_config['threshold'] -= 5
    elif mode == 'economy':
        base_config['hysteresis'] += 3
    
    # Extra computations for distraction
    adjustment_factor = 1.0
    for i in range(2):
        adjustment_factor *= 0.95 if i == 0 else 1.05
    
    # Dead code path (never executed in normal flow)
    debug_trace = []
    for j in range(3):
        debug_trace.append(f'step_{j}')
    
    return base_config['threshold']

# Core evaluation logic with interdependent steps
def evaluate_performance(metrics, baseline):
    readings = metrics['readings']
    count = metrics['count']
    total = sum(readings)
    
    # Multiple intermediate variables, some unused later
    peak = max(readings)
    floor = min(readings)
    range_spread = peak - floor
    
    # Secondary distractor calculation
    outlier_count = 0
    deviations = []
    for r in readings:
        dev = abs(r - baseline)
        deviations.append(dev)
        if dev > 15:
            outlier_count += 1
    
    # Normalized performance index (unused)
    norm_index = (total / (baseline * count)) if baseline else 0
    
    # Key decision logic depending on multiple factors
    if count > 5 and total > 500:
        if peak > baseline + 10:
            multiplier = 1.2
        else:
            multiplier = 1.0
    else:
        multiplier = 0.8
    
    # Final computation chain
    base_score = total * 0.1
    adjusted = base_score * multiplier
    penalty = 0
    
    # Conditional penalty based on spread
    if range_spread > 40:
        penalty = 5
    elif range_spread < 20:
        penalty = -2  # bonus
    
    final_score = int(adjusted - penalty)  # critical assignment point
    
    # Additional unrelated tracking
    stats_summary = defaultdict(list)
    stats_summary['values'].extend(readings)
    stats_summary['deviations'].extend(deviations)
    
    return final_score

# Main execution sequence
if __name__ == '__main__':
    metrics = collect_metrics()
    baseline = calibrate_system('standard')
    final_score = evaluate_performance(metrics, baseline)
    print(f'Result: {final_score}')