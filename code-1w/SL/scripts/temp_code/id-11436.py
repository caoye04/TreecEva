import itertools

def preprocess_readings(raw_sensors):
    filtered = [x for x in raw_sensors if 0 <= x <= 100]
    smoothed = [(filtered[i] + filtered[i+1]) / 2 for i in range(len(filtered)-1)]
    return [round(val, 2) for val in smoothed]

def generate_combinations(elements):
    # Irrelevant helper: generates pairs but not used in main logic
    return list(itertools.combinations(elements, 2))

def normalize_range(values, old_min=0, old_max=100, new_min=0, new_max=1):
    if not values:
        return []
    return [(v - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for v in values]

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified mock entropy
    return round(entropy, 4)

def evaluate_performance(weights, data_sequence):
    base_scores = []
    for idx, segment in enumerate(data_sequence):
        trend = sum(segment[i] < segment[i+1] for i in range(len(segment)-1))
        stability = sum(abs(segment[i] - segment[i+1]) for i in range(len(segment)-1))
        score = (trend * weights['trend']) - (stability * weights['volatility'])
        base_scores.append(score)
    
    # Dummy distraction: unused complex calculation
    all_pairs = list(itertools.product(base_scores, repeat=2))
    pair_deltas = [abs(a - b) for a, b in all_pairs if a != b]
    avg_delta = sum(pair_deltas) / len(pair_deltas) if pair_deltas else 0
    
    # Actual path to answer
    raw_aggregate = sum(base_scores)
    adjustment_factor = len(data_sequence) * weights['consistency']
    final_score = raw_aggregate + adjustment_factor
    
    # More distractions
    max_pair = max(all_pairs, default=(0,0))
    phantom_check = max_pair[0] * 0.1 if max_pair[0] > 5 else 0
    
    return int(round(final_score + phantom_check))

# Main execution
raw_sensor_data = [85, 90, 95, 105, 92, 88, 76, 81, 87, 93, 101, 97, 94]
cleaned_data = preprocess_readings(raw_sensor_data)
segments = [cleaned_data[i:i+3] for i in range(0, len(cleaned_data), 3) if len(cleaned_data[i:i+3]) == 3]
normalized_data = [normalize_range(seg) for seg in segments]

# Unused combinatorics - adds interference
all_combinations = generate_combinations([1, 2, 3, 4])

metric_weights = {
    'trend': 1.5,
    'volatility': 0.25,
    'consistency': 2
}

entropy_diagnostic = calculate_entropy([int(x*100) for sublist in normalized_data for x in sublist])

# Key statement
final_score = evaluate_performance(metric_weights, normalized_data)

print(f"Result: {final_score}")