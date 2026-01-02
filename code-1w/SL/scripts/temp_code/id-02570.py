from collections import defaultdict, Counter
import math

# Simulated health monitoring system with multiple sensor streams
def simulate_vital_signs():
    return {
        'heart_rate': [72, 75, 78, 80, 68, 74],
        'oxygen': [98.2, 97.5, 96.8, 99.1, 95.6, 97.0],
        'temperature': [36.6, 37.1, 36.9, 37.3, 36.8, 37.0],
        'respiration': [16, 18, 17, 19, 16, 18]
    }

def analyze_trend(data_list):
    # Irrelevant trend analysis (distractor)
    diffs = [data_list[i+1] - data_list[i] for i in range(len(data_list)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

def calculate_entropy(values):
    # Unused entropy function (dead code path)
    counts = Counter(values)
    total = len(values)
    return -sum((count/total) * math.log2(count/total) for count in counts.values())

def normalize_readings(readings):
    # Normalization logic that's not actually used in final calculation (red herring)
    normalized = {}
    for key, values in readings.items():
        mean_val = sum(values) / len(values)
        normalized[key] = [v - mean_val for v in values]
    return normalized

def filter_outliers(data_seq, limit=3):
    # Outlier filtering not used in main path (misleading intermediate)
    avg = sum(data_seq) / len(data_seq)
    dev = math.sqrt(sum((x - avg)**2 for x in data_seq) / len(data_seq))
    return [x for x in data_seq if abs(x - avg) <= limit * dev]

def compute_stress_index(hr_vals, temp_vals):
    # Secondary metric not directly used (distractor computation)
    hr_avg = sum(hr_vals) / len(hr_vals)
    temp_avg = sum(temp_vals) / len(temp_vals)
    stress_score = (hr_avg * 0.6) + (temp_avg * 0.4)
    return round(stress_score, 2)

def evaluate_consistency(data_map):
    # Consistency check with decoy logic
    consistency = defaultdict(float)
    for k, v in data_map.items():
        changes = sum(1 for i in range(1, len(v)) if abs(v[i] - v[i-1]) > 1.0)
        consistency[k] = changes / (len(v) - 1) if len(v) > 1 else 0
    return dict(consistency)

def aggregate_risk_levels(metrics):
    # Complex aggregation not used in final answer (layer of distraction)
    risk_map = {}
    for metric, values in metrics.items():
        high_count = sum(1 for v in values if v > {'heart_rate': 75, 'oxygen': 97.0, 'temperature': 37.0}.get(metric, 0))
        risk_map[metric] = 'high' if high_count >= 3 else 'moderate' if high_count == 2 else 'low'
    return risk_map

def derive_pattern_signature(values):
    # Bit manipulation red herring
    signature = 0
    for v in values[:4]:
        shifted = int(v) << 2
        signature ^= shifted
    return signature & 0xFFFF

def process_metrics(data, thresholds):
    # Core relevant logic buried within distractions
    results = defaultdict(float)
    
    # Real computation path begins here
    hr = data['heart_rate']
    o2 = data['oxygen']
    temp = data['temperature']
    resp = data['respiration']
    
    # Key intermediate: average oxygen saturation
    avg_o2 = sum(o2) / len(o2)
    
    # Hidden dependency: count how many temps above threshold
    fever_count = sum(1 for t in temp if t > thresholds['temperature'])
    
    # Critical step: weighted combination based on specific indices
    index_weight = 0
    for i in range(len(hr)):
        if i % 2 == 0:  # Only even indices matter
            index_weight += hr[i] * (o2[-(i+1)] / 10)  # Reverse indexing on oxygen
    
    # Distractor: unused complex transformation
    transformed = [math.sin(math.radians(x)) for x in resp]
    
    # Actual final computation
    base_score = index_weight / 100
    adjustment = fever_count * thresholds['fever_penalty']
    final_risk = base_score - adjustment
    
    # Final diagnostic is derived from manipulated arithmetic
    final_diagnostic = int(abs(final_risk * 10)) * 2 - 15
    
    # Irrelevant return of other values (decoy outputs)
    debug_info = {
        'base': base_score,
        'adjust': adjustment,
        'index_wt': index_weight
    }
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    
    # Simulate input data
    health_data = simulate_vital_signs()
    
    # Define threshold map (only some keys are actually used)
    threshold_map = {
        'heart_rate': 75,
        'oxygen': 97.0,
        'temperature': 36.8,  # Used
        'respiration': 18,
        'fever_penalty': 2.5  # Used
    }
    
    # Call core processing function
    final_diagnostic = process_metrics(health_data, threshold_map)
    
    # Unused variables - red herrings
    trend_analysis = {k: analyze_trend(v) for k, v in health_data.items()}
    entropy_values = {k: calculate_entropy(v) for k, v in health_data.items()}
    normalized_data = normalize_readings(health_data)
    stress_index = compute_stress_index(health_data['heart_rate'], health_data['temperature'])
    consistency_report = evaluate_consistency(health_data)
    risk_levels = aggregate_risk_levels(health_data)
    pattern_codes = {k: derive_pattern_signature(v) for k, v in health_data.items()}
    
    # Output only the target result
    print(f"Target result: {final_diagnostic}")