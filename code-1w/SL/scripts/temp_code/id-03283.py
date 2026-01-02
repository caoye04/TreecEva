import itertools

def analyze_efficiency(data, threshold):
    filtered = [x for x in data if x > threshold]
    temp_sum = sum(filtered) * 0.85
    avg = temp_sum / len(filtered) if filtered else 0
    return avg

def compute_variance(values):
    mean = sum(values) / len(values) if values else 0
    squared_diffs = [(v - mean) ** 2 for v in values]
    variance = sum(squared_diffs) / len(squared_diffs) if squared_diffs else 0
    return variance

def generate_metrics(raw):
    scaled = [x * 1.1 for x in raw]
    noise = [0.1 * i for i in range(len(scaled))]
    perturbed = [scaled[i] + noise[i] for i in range(len(scaled))]
    return perturbed

def validate_stability(readings):
    if len(readings) < 3:
        return False
    deltas = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    return all(d < 5 for d in deltas)

def evaluate_performance(metrics, base):
    adjusted = [m - base for m in metrics]
    positive_count = len([x for x in adjusted if x > 0])
    total_impact = sum(adjusted)
    
    # Irrelevant transformations (distractors)
    decoy_map = {i: val * 0.95 for i, val in enumerate(metrics)}
    decoy_pairs = list(itertools.combinations(metrics, 2))
    decoy_sums = [a + b for a, b in decoy_pairs if a > b]
    fake_aggregate = sum(decoy_sums) / len(decoy_sums) if decoy_sums else 0
    
    # Dead code path (never executed due to condition)
    special_bonus = 0
    if len(metrics) > 100:
        reference_groups = list(itertools.groupby(metrics, key=lambda x: x // 10))
        group_counts = {k: len(list(g)) for k, g in reference_groups}
        special_bonus = sum(group_counts.values()) * 0.1
    
    # Core logic hidden among distractions
    performance_tier = 'high' if positive_count >= 4 else 'low'
    tier_multiplier = 1.5 if performance_tier == 'high' else 0.7
    
    # Another red herring: complex but unused calculation
    shadow_index = 0
    for i in range(len(metrics)):
        for j in range(i+1, len(metrics)):
            if metrics[i] < metrics[j]:
                shadow_index += (j - i) * 0.1
    
    # Actual answer computation buried here
    base_offset = base * 0.2
    raw_score = total_impact * tier_multiplier + base_offset
    final_score = int(round(raw_score))  # Critical assignment point
    
    # More misleading output (not affecting result)
    diagnostic = {
        'peak': max(metrics, default=0),
        'volatility': compute_variance(metrics),
        'consistency': validate_stability(metrics)
    }
    
    return final_score

def main():
    # Real input data
    sensor_data = [12, 15, 10, 18, 22, 14, 16]
    baseline = 13
    
    # Distractor variables and operations
    dummy_data = [x ** 0.5 for x in sensor_data if x % 2 == 0]
    auxiliary_map = {f'idx_{i}': val * 2 for i, val in enumerate(sensor_data)}
    temp_analysis = analyze_efficiency(sensor_data, threshold=11)
    
    processed = generate_metrics(sensor_data)
    
    # Unused complex structure
    metadata_cube = [
        [[i+j+k for k in range(3)] for j in range(2)] 
        for i in range(len(sensor_data))
    ]
    
    # Key execution point
    final_score = evaluate_performance(processed, baseline)
    
    # Print required result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()