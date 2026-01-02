from collections import defaultdict, Counter

# Simulated system performance metrics
def generate_metrics():
    return {
        'latency': [120, 135, 110, 145, 95],
        'throughput': [880, 920, 850, 900, 930],
        'errors': [3, 1, 4, 0, 2],
        'peaks': (150, 940)
    }

def analyze_trends(data):
    # Irrelevant trend analysis (dead function - never used)
    trends = {}
    for key, values in data.items():
        if isinstance(values, list):
            avg = sum(values) / len(values)
            trend = 'improving' if values[-1] < avg else 'declining'
            trends[key] = trend
    return trends

def validate_inputs(raw_data):
    # Superfluous validation with side effects
    issues = []
    for k, v in raw_data.items():
        if 'errors' in k and any(e < 0 for e in v if isinstance(v, list)):
            issues.append(f'Negative error count in {k}')
    return len(issues) == 0

def compute_baseline(series, mode='avg'):
    # Distractor: multiple modes, only one used
    if mode == 'avg':
        return sum(series) // len(series)
    elif mode == 'max':
        return max(series)
    else:
        return min(series)

def extract_key_indicators(metrics):
    # Extracts real features but includes red herring computations
    latency_base = compute_baseline(metrics['latency'], 'avg')
    throughput_peak = compute_baseline(metrics['throughput'], 'max')  # Unused
    error_count = sum(metrics['errors'])

    # Misleading intermediate calculation (never used)
    peak_latency_ratio = metrics['peaks'][0] / latency_base

    # Real signal
    stable_periods = sum(1 for x in metrics['latency'] if x <= 120)

    return {
        'base_lat': latency_base,
        'err_total': error_count,
        'stable_windows': stable_periods
    }

def build_efficiency_map(indicators):
    # Creates mapping that will be used later
    efficiency_map = defaultdict(float)
    efficiency_map['latency_factor'] = 100 / indicators['base_lat']
    efficiency_map['error_penalty'] = 0.1 * indicators['err_total']
    efficiency_map['stability_bonus'] = 0.05 * indicators['stable_windows']
    
    # Decoy entries
    efficiency_map['phantom_metric_1'] = 999
    efficiency_map['phantom_metric_2'] = -1
    
    return efficiency_map

def calculate_weighted_index(data, weights):
    # Complex weighting with irrelevant branches
    index = 0.0
    components = []
    
    for k, v in weights.items():
        if 'phantom' in k:
            # Dead branch: these are distractors
            temp_val = v * 0.01
            components.append(temp_val)
            continue
        if 'latency' in k:
            index += v * data['base_lat']
        elif 'penalty' in k:
            index -= v * 10
        elif 'bonus' in k:
            index += v * 20
    
    # Final adjustment based on unused trend
    anomaly_flag = False  # Never set True
    if anomaly_flag:
        index *= 0.9
    
    return round(index, 4)

def assess_reliability(metrics):
    # Independent path: computes something plausible but unused
    c = Counter(metrics['errors'])
    freq_zero = c[0]
    return freq_zero >= 2

def process_performance(metrics, efficiency_map):
    # Core logic buried in noise
    indicators = extract_key_indicators(metrics)
    
    # Real computation chain starts here
    raw_index = calculate_weighted_index(indicators, efficiency_map)
    
    # Secondary transformation
    adjustment = 0
    if indicators['err_total'] < 5:
        adjustment += 15
    if indicators['stable_windows'] > 2:
        adjustment += 10
    
    # Critical line: this is where final_score is assigned
    final_score = int(raw_index) + adjustment
    
    # Red herring: fake refinement (not assigned back)
    if final_score > 100:
        refined = final_score * 0.95
    
    # Dead code block
    unused_buffer = []
    for i in range(3):
        unused_buffer.append({'frame': i, 'status': 'idle'})
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Step 1: Generate raw data
    raw_system_data = generate_metrics()
    
    # Step 2: Validate (useless check)
    is_valid = validate_inputs(raw_system_data)
    
    # Step 3: Extract meaningful indicators
    key_indicators = extract_key_indicators(raw_system_data)
    
    # Step 4: Build efficiency map with decoys
    efficiency_map = build_efficiency_map(key_indicators)
    
    # Step 5: Assess reliability (result not used)
    system_reliable = assess_reliability(raw_system_data)
    
    # Step 6: Process performance to get final score
    final_score = process_performance(raw_system_data, efficiency_map)
    
    # Output result
    print(f"Result: {final_score}")