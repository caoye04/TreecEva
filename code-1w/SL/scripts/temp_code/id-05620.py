import math

def analyze_efficiency(data, threshold=0.75):
    """Irrelevant analysis function (dead code path)"""
    if not data:
        return 0
    avg = sum(data) / len(data)
    return avg > threshold

def preprocess_signal(signal):
    """Another red herring - unused in main logic"""
    normalized = [x / max(signal) for x in signal if x > 0]
    filtered = list(filter(lambda x: x > 0.1, normalized))
    return [round(x, 3) for x in filtered]

def transform_metrics(raw):
    # Relevant but obfuscated transformation
    transformed = {}
    for k, v in raw.items():
        if 'count' in k:
            transformed[k] = v * 1.5 if v % 2 else v * 0.8
        elif 'time' in k:
            transformed[k] = math.log(v + 1) if v > 0 else 0
        else:
            transformed[k] = abs(v - 10)  # distractor logic
    return transformed

def calculate_robustness(indices):
    # Decoy computation with misleading intermediate result
    total = 0
    for i in indices:
        if i % 3 == 0:
            total += i * 2
        elif i % 5 == 0:
            total -= i  # irrelevant adjustment
    return total // 2  # unused return value

def evaluate_performance(metrics, base):
    # Core logic embedded in noise
    temp_results = []
    weights = {'throughput_count': 0.4, 'latency_time': 0.35, 'error_count': -0.2, 'retries_count': 0.1}
    
    # Distractor variables
    debug_trace = []
    anomaly_detected = False
    cumulative_offset = 0
    
    for key, val in metrics.items():
        if key not in weights:
            continue
        weight = weights[key]
        contribution = val * weight
        temp_results.append(contribution)
        
        # Fake branching logic
        if contribution < 0:
            debug_trace.append(f"Negative: {contribution}")
            anomaly_detected = True
        
        # Useless accumulation
        cumulative_offset += len(str(int(val)))
    
    # Real aggregation
    raw_sum = sum(temp_results)
    
    # Fake normalization chain
    if raw_sum > base:
        adjusted = raw_sum * (1.1 - 0.01 * len(temp_results))
    else:
        adjusted = raw_sum * (0.9 + 0.02 * len([x for x in temp_results if x > 0]))
    
    # Final manipulation using string method (required feature)
    str_adjusted = str(adjusted).replace('.', '')
    checksum = sum(int(d) for d in str_adjusted if d.isdigit())
    
    # Key assignment: this is the answer
    final_score = int(round(adjusted + checksum * 0.1))
    
    # Dead code - never reached due to logic
    if anomaly_detected and False:
        fallback = sum(debug_trace.count(x) for x in debug_trace)
        return fallback
        
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data with mixed relevance
    metrics_data = {
        'throughput_count': 120,
        'latency_time': 45,
        'error_count': 8,
        'retries_count': 3,
        'timestamp': 1678886400,  # irrelevant
        'version_id': 'v2.1.5'     # irrelevant
    }
    
    baseline_ref = 40
    
    # Unused complex structure
    signal_input = [0.1, -0.5, 0.8, 0.0, 1.2, 0.9]
    processed = preprocess_signal(signal_input)
    
    # Irrelevant combinatorics
    index_set = [i for i in range(1, 10) if i % 2]
    robustness_metric = calculate_robustness(index_set)
    
    # Transform step that looks important but isn't fully used
    transformed_metrics = transform_metrics(metrics_data)
    
    # Key execution point
    final_score = evaluate_performance(metrics_data, baseline_ref)
    
    # Output requirement
    print(f"Result: {final_score}")