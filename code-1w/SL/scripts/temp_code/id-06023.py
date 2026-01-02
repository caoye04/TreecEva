from collections import defaultdict, Counter
import math

def analyze_signal_strength(signal_data):
    # Irrelevant function: simulates signal analysis
    histogram = defaultdict(int)
    for val in signal_data:
        histogram[round(val / 10) * 10] += 1
    return dict(histogram)

def compute_entropy(arr):
    # Misleading computation: not used in final result
    freq = Counter(arr)
    total = len(arr)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def evaluate_consistency(logs):
    # Dead code path: looks important but unused
    transitions = 0
    for i in range(1, len(logs)):
        if logs[i] != logs[i-1]:
            transitions += 1
    return transitions > len(logs) * 0.3

def filter_outliers(data, threshold=1.5):
    # Distractor: modifies a copy, not used later
    median = sorted(data)[len(data)//2]
    filtered = [x for x in data if abs(x - median) < threshold * 10]
    return filtered

def calculate_baseline(readings):
    # Relevant but indirect: used to derive base_offset
    avg = sum(readings) / len(readings)
    deviation = sum(abs(r - avg) for r in readings) / len(readings)
    return int(avg - deviation)

def generate_weight_map(keys):
    # Creates decoy weights; actual weights are hardcoded later
    weight_map = {k: hash(k) % 10 for k in keys}
    normalized = {k: v / sum(weight_map.values()) for k in weight_map}
    return normalized

def aggregate_performance(metrics, weights):
    # CORE LOGIC: this is where final_score is computed
    temp_store = defaultdict(float)
    scaling_factor = 1.75
    
    # Step 1: Apply weights with conditional adjustment
    for key in metrics:
        raw_val = metrics[key]
        weight = weights.get(key, 0.1)
        
        # Conditional boost for high performers
        adjusted_val = raw_val * scaling_factor
        if adjusted_val > 85:
            adjusted_val *= 1.1  # bonus
        
        temp_store[key] = adjusted_val * weight
    
    # Step 2: Accumulate weighted contributions
    total_contribution = 0.0
    for val in temp_store.values():
        total_contribution += val
    
    # Step 3: Apply penalty if any metric below threshold
    min_metric = min(metrics.values())
    penalty = 0
    if min_metric < 60:
        penalty = 15
    
    # Step 4: Final adjustment using bit manipulation (obscure but relevant)
    # Simulates hardware-level adjustment
    base_int = int(total_contribution)
    masked = base_int & ~((1 << 3) - 1)  # Clear lower 3 bits
    shifted = masked >> 2
    
    # FINAL RESULT
    final_score = shifted - penalty
    
    # Irrelevant print for distraction
    print(f'Debug: masked={masked}, shifted={shifted}')
    return int(final_score)

# MAIN EXECUTION
if __name__ == '__main__':
    # INPUT DATA
    sensor_readings = [88, 76, 92, 81, 79, 85, 90]
    activity_logs = [1, 1, 0, 1, 1, 1, 0, 0, 1]
    signal_data = [120, 130, 125, 140, 135, 150, 145]

    # DEAD VARIABLE ASSIGNMENTS - DISTRACTORS
    entropy_value = compute_entropy(sensor_readings)  # Unused
    consistency_flag = evaluate_consistency(activity_logs)  # Unused
    cleaned_signals = filter_outliers(signal_data)  # Unused
    histogram_data = analyze_signal_strength(signal_data)  # Unused

    # DERIVED BASE VALUE (used indirectly via offset)
    base_offset = calculate_baseline(sensor_readings)

    # RED HERRING WEIGHT GENERATION
    fake_weights = generate_weight_map(['accuracy', 'speed', 'reliability'])  # Not used

    # ACTUAL METRICS AND WEIGHTS
    metrics = {
        'accuracy': 92 + base_offset % 5,      # evaluates to 92 + 76%5 = 92+1 = 93
        'speed': 88,
        'reliability': 78,
        'latency': 65
    }

    weights = {
        'accuracy': 0.4,
        'speed': 0.3,
        'reliability': 0.2,
        'latency': 0.1
    }

    # CRITICAL STATEMENT
    final_score = aggregate_performance(metrics, weights)
    
    # OUTPUT RESULT
    print(f'Result: {final_score}')