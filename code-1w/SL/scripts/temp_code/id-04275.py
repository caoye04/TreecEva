import math

# Simulated sensor data processing with diagnostic overlays
def collect_diagnostics(mode='advanced'):
    readings = [18, 22, 15, 30, 12]
    diagnostics = {}
    
    for i, val in enumerate(readings):
        diagnostics[f'sensor_{i}'] = {
            'raw': val,
            'calibrated': val * 1.05 + 2,
            'status': 'OK' if val > 14 else 'ERROR'
        }
    
    # Irrelevant aggregation (distractor)
    error_count = sum(1 for d in diagnostics.values() if d['status'] == 'ERROR')
    system_health = 100 - (error_count * 10)
    
    return diagnostics

# Legacy function - unused but looks important (dead code path)
def legacy_calibrate(x):
    if isinstance(x, list):
        return [legacy_transform(v) for v in x]
    return x * 0.9 + 1.5

def legacy_transform(n):
    return (n ** 2) / 3.7

# Core processing pipeline
def generate_baseline(data_stream):
    # Apply non-linear transformation
    processed = [round(math.log(d + 1) * 3.2, 2) for d in data_stream]
    
    # Group by ranges (irrelevant grouping distractor)
    groups = {i: [] for i in range(5)}
    for p in processed:
        bucket = min(int(p // 5), 4)
        groups[bucket].append(p)
    
    # Real computation buried here
    base_metric = sum(processed) / len(processed)
    return base_metric

def evaluate_thresholds(config, offset=0.75):
    thresholds = []
    for k, v in config.items():
        if 'limit' in k:
            adjusted = v * offset
n            if adjusted > 10:
                adjusted = 10
            elif adjusted < 0:
                adjusted = 0
            thresholds.append(round(adjusted, 2))
    
    # Red herring: complex-looking normalization
    normalized = [math.sin(t / 10) * 100 for t in thresholds]
    avg_norm = sum(normalized) / len(normalized)
    
    return thresholds  # Actual return used later

def process_metrics(summary, factor):
    # Unpack summary tuple
    avg_val, peak, count = summary
    
    # Meaningful calculation
    signal_quality = avg_val * (peak / 100) * count
    
    # Distractor: complex conditional expression using string methods
    category = 'A' if str(signal_quality).count('5') > 0 else 'B'
    bonus = 15 if 'A' in category and signal_quality > 200 else 5
    
    # Multiple assignments (tuple unpacking)
    multiplier, penalty = (1.8, 0) if signal_quality > 250 else (1.4, 12)
    
    # Core formula
    score = (signal_quality * factor * multiplier) - penalty + bonus
    
    # Decoy logic that looks important but unused
    audit_trail = []
    audit_trail.append(f'Final score before flooring: {score}')
    audit_trail.append(f'Source count: {count}')
    final_score = int(score)  # Critical assignment point
    
    # Unused comprehensive log (distractor)
    log_entry = {
        'timestamp': '2023-12-05',
        'operation': 'metric_processing',
        'inputs': {'avg': avg_val, 'peak': peak, 'count': count},
        'factors': {'factor': factor, 'multiplier': multiplier},
        'result_raw': score,
        'result_final': final_score
    }
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    raw_input_stream = [45, 67, 52, 81, 44, 73, 58]
    config_settings = {
        'limit_upper': 18.5,
        'limit_lower': 3.2,
        'window_size': 5
    }
    calibration_factor = 0.88
    
    # Step 1: Generate baseline from stream
    avg_baseline = generate_baseline(raw_input_stream)
    
    # Step 2: Extract key metrics
    peak_signal = max(raw_input_stream)
    sample_count = len(raw_input_stream)
    
    # Create summary tuple (critical data structure)
    data_summary = (avg_baseline, peak_signal, sample_count)
    
    # Step 3: Evaluate thresholds (used to mislead)
    active_thresholds = evaluate_thresholds(config_settings, offset=0.85)
    
    # Step 4: Collect diagnostics (irrelevant call - distractor)
    health_report = collect_diagnostics(mode='advanced')
    
    # Step 5: Process final metrics
    final_score = process_metrics(data_summary, calibration_factor)
    
    # Output target result
    print(f"Target result: {final_score}")