from collections import defaultdict, Counter
import math

def analyze_frequency(data):
    # Irrelevant function: analyzes character frequency in string representations
    freq = defaultdict(int)
    for item in data:
        for c in str(item):
            if c.isdigit():
                freq[c] += 1
    return dict(freq)

def compute_checksum(sequence):
    # Misleading computation: looks important but unused later
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1)
    return checksum % 1000

def normalize_vector(vec):
    # Dead code path: never called
    magnitude = sum(x ** 2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

def filter_outliers(data, threshold=2):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def transform_metrics(raw):
    # Relevant transformation with distractors
    transformed = {}
    temp_store = []
    
    for k, v in raw.items():
        if 'latency' in k:
            transformed[k] = round(1000 / (v + 1e-8), 3)  # inverse latency as speed
        elif 'throughput' in k:
            adjusted = v * 0.9
            temp_store.append(adjusted)  # red herring storage
            transformed[k] = adjusted
    
    # Decoy aggregation
    dummy_avg = sum(temp_store) / len(temp_store) if temp_store else 0
    transformed['dummy_baseline'] = dummy_avg
    
    return transformed

def evaluate_component_health(values):
    # Complex logic that feeds into final result
    health_scores = []
    for val in values:
        if val < 50:
            score = 20
        elif val < 80:
            score = 60
        else:
            score = 95
        noise = int((val * 0.05) // 1)  # minor deterministic perturbation
        health_scores.append(score + noise)
    return health_scores

def calculate_weighted_risk(profile):
    # Unused risk model — misleading complexity
    weights = {'critical': 3, 'high': 2, 'medium': 1}
    total_risk = 0
    for level, count in profile.items():
        total_risk += weights.get(level, 0) * count
    return total_risk * 10

def evaluate_performance(metrics, reference):
    # Core logic buried in distractions
    base_values = [v for k, v in metrics.items() if 'throughput' in k or 'latency' in k]
    
    # Apply health scoring
    health_list = evaluate_component_health(base_values)
    
    # Real computation begins here
    aggregate_health = sum(health_list)
    
    # Destructuring relevant parts from reference
    ref_stats = [v for k, v in reference.items() if 'ref_' in k]
    offset = ref_stats[0] * 0.1  # use first reference value as scaling anchor
    
    # Bit manipulation decoy
    magic_flag = 0b1010
    magic_flag ^= 0b1100
    magic_flag &= ~0b0010
    
    # Actual key step: combine health with scaled reference
    trend_factor = (aggregate_health + offset) / 100
    
    # Conditional adjustment based on hidden rule
    if len(base_values) > 1 and base_values[0] > base_values[1]:
        trend_factor *= 1.1
    else:
        trend_factor *= 0.95
    
    # Final mapping through logarithmic correction
    final = int(math.log(trend_factor ** 2 + 1e-5, 2)) * 10
    
    # Irrelevant printing (simulates debugging noise)
    debug_info = f"Final trend: {trend_factor:.2f}, Flag: {magic_flag:b}"
    
    return final

# Main execution block
if __name__ == '__main__':
    # Input data setup
    metrics = {
        'latency_primary': 12,
        'latency_backup': 45,
        'throughput_main': 88,
        'throughput_aux': 63,
        'power_draw': 150,
        'temperature_peak': 78
    }

    benchmark_data = {
        'ref_base': 40,
        'ref_scale': 1.5,
        'ref_bias': 20
    }

    # Irrelevant preprocessing
    freq_analysis = analyze_frequency(list(metrics.values()))
    chk = compute_checksum([10, 20, 30, 40])  # unused result

    # Transform metrics (contains red herrings)
    processed_metrics = transform_metrics(metrics)

    # Filter outliers in a subset (partially used, partially not)
    filtered_throughputs = filter_outliers([metrics['throughput_main'], metrics['throughput_aux']])

    # Hidden control flow: this condition is false, so dead branch
    mode_flag = 'aggressive'
    if mode_flag == 'experimental':
        fallback_value = calculate_weighted_risk({'high': 2, 'medium': 4})

    # Key statement
    final_score = evaluate_performance(processed_metrics, benchmark_data)

    # Output result as required
    print(f"Result: {final_score}")