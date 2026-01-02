from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring station
def collect_readings():
    return [23.4, 24.1, 19.5, 25.0, 30.2, 28.6, 24.3, 21.0, 18.9, 26.7]

def filter_outliers(data, threshold=2.5):
    mean = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean) / mean < threshold]
    return filtered

def compute_rolling_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def generate_checksum(sequence):
    # Irrelevant function - decoy for data integrity focus
    checksum = 0
    for val in sequence:
        checksum ^= int(val * 10) & 0xFF
    return checksum

def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.5 for _ in readings]
    return [(r - min_val) / (max_val - min_val) for r in readings]

def calculate_entropy(values):
    # Misleading complexity: not actually used in final result
    counts = Counter([round(v, 1) for v in values])
    total = len(values)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def assess_trend(stability_index):
    # Dead code path - never called
    if stability_index > 0.8:
        return "stable"
    elif stability_index > 0.5:
        return "fluctuating"
    else:
        return "unreliable"

def evaluate_performance(metrics, base):
    temp_var = metrics['smoothness'] * 1.05
    if metrics['consistency'] < base['consistency']:
        temp_var -= 0.1
    adjustment = 0.0
    
    # Key logic chain with distractions
    raw_scores = []
    for key in ['stability', 'uniformity', 'coherence']:
        score = metrics.get(key, 0.0) * base.get(key, 1.0)
        raw_scores.append(score)
        
    # Distractor: complex transformation not affecting final result
    transformed = defaultdict(float)
    for i, s in enumerate(raw_scores):
        transformed[f'score_{i}'] = math.sin(s) ** 2 + math.cos(s) ** 2  # Always 1
    
    # Real computation buried in noise
    primary = sum(raw_scores) * metrics['coverage']
    secondary = metrics['efficiency'] * 100
    
    # Critical statement with slicing red herring
    history = [primary * 0.9, primary, primary * 1.1]
    recent = history[-2:]  # Looks important but unused
    
    # Actual determination
    if metrics['valid_points'] >= 8:
        adjustment += 5.0
    if metrics['outlier_rate'] < 0.15:
        adjustment += 3.5
    
    # Final calculation
    result = primary + secondary + adjustment
    
    # Multiple assignments distraction
    temp_a, temp_b = result * 0.99, result * 1.01
    temp_c = (temp_a + temp_b) / 2
    
    # Answer is here
    final_score = int(round(result))
    
    # Unused but plausible-looking outputs
    diagnostics = {
        'checksum': generate_checksum([result]),
        'entropy': calculate_entropy([primary, secondary, adjustment])
    }
    
    return final_score

# Main execution flow
readings = collect_readings()
baseline_metrics = filter_outliers(readings)
avgs = compute_rolling_average(baseline_metrics)
normalized = normalize_readings(baseline_metrics)

# Irrelevant data structures
stats_summary = {
    'count': len(normalized),
    'mean': sum(normalized) / len(normalized),
    'range': max(normalized) - min(normalized)
}

# Construct input for evaluation - this is what matters
sample_metrics = {
    'stability': 0.87,
    'uniformity': 0.76,
    'coherence': 0.91,
    'consistency': 0.82,
    'coverage': 1.2,
    'efficiency': 0.68,
    'smoothness': 0.74,
    'valid_points': 9,
    'outlier_rate': 0.12
}

baseline_config = {
    'stability': 1.05,
    'uniformity': 1.02,
    'coherence': 0.95,
    'consistency': 0.85
}

# Key statement
final_score = evaluate_performance(sample_metrics, baseline_config)
print(f"Result: {final_score}")