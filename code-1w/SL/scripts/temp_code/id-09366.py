import itertools

def analyze_sensor_readings(readings):
    filtered = [r for r in readings if r > 25 and r < 95]
    squared_devs = [(x - 60) ** 2 for x in filtered]
    avg_sq_dev = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return avg_sq_dev

def compute_checksum(sequence):
    # Irrelevant function - decoy
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val + i) % 256
    return checksum

def transform_coordinates(coords):
    # Unused transformation - dead code path
    return [(y * 2, x // 2) for x, y in coords]

def generate_pairs(values):
    # Distractor using itertools
    pairs = list(itertools.combinations(values, 2))
    weighted = [abs(a - b) * (i % 7) for i, (a, b) in enumerate(pairs)]
    return sum(weighted) // len(weighted) if weighted else 0

def validate_sequence(seq):
    # Misleading validation logic
    if len(seq) < 5:
        return False
    cumulative = 0
    for num in seq:
        if num % 3 == 0:
            cumulative += num
        elif num % 7 == 0:
            cumulative -= num
    return cumulative > 100

def process_time_series(data):
    # Relevant but partially obscured logic
    window_size = 4
    trends = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        increasing = all(window[j] < window[j+1] for j in range(len(window)-1))
        decreasing = all(window[j] > window[j+1] for j in range(len(window)-1))
        if increasing:
            trends.append(1)
        elif decreasing:
            trends.append(-1)
    trend_score = sum(trends) * 17
    return trend_score

def calculate_entropy(values):
    # Red herring with complex math
    from math import log2
    if not values:
        return 0.0
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def calculate_final_score(dataset):
    # Core logic hidden among distractions
    base_value = sum(dataset) % 1000
    
    # Irrelevant intermediate
    temp_map = {i: dataset[i] * (i + 1) for i in range(len(dataset))}
    dummy_agg = max(temp_map.values()) - min(temp_map.values())
    
    # Key transformation
    adjusted = [x * 1.5 for x in dataset if x % 2 == 1]  # Only odd values scaled
    adjustment_factor = len(adjusted)
    
    # Secondary relevant path
    peak_count = sum(1 for i in range(1, len(dataset)-1)
                     if dataset[i-1] < dataset[i] > dataset[i+1])
    
    # Real computation chain
    raw_sum = sum(adjusted)
    modifier = 3 if peak_count >= 2 else 5
    final_score = int(raw_sum * modifier - base_value)
    
    # Dead branch - never executed due to logic
    if dummy_agg < 0:
        fallback = calculate_entropy(dataset)
        final_score = int(fallback * 100)
    
    return final_score

# Main execution flow
if __name__ == '__main__':
    raw_input_stream = [42, 63, 28, 77, 55, 19, 84, 36, 71, 50]
    metadata_tags = ['A1', 'B2', 'C3', 'D4', 'E5']  # Unused
    config_threshold = 68  # Distractor constant
    
    # Sensor analysis (partially relevant)
    noise_floor = analyze_sensor_readings(raw_input_stream)
    
    # Coordinate decoy
    coordinates = [(12, 34), (56, 78), (91, 23)]
    transformed_coords = transform_coordinates(coordinates)
    
    # Time series processing - actually used later
    trend_strength = process_time_series(raw_input_stream)
    
    # Checksum calculation - irrelevant
    stream_checksum = compute_checksum(raw_input_stream)
    
    # Entropy computation - red herring
    uncertainty_metric = calculate_entropy(raw_input_stream)
    
    # Pair generation with itertools - distractor
    pair_weight_score = generate_pairs([10, 20, 30, 40])
    
    # Validation check - unused result
    is_valid = validate_sequence(raw_input_stream)
    
    # Critical preprocessing step disguised as generic
    processed_data = [x + (i % 3) for i, x in enumerate(raw_input_stream)]
    processed_data = [x for x in processed_data if x not in [43, 78, 85]]  # Filter out modified values
    
    # Key assignment - the target statement
    final_score = calculate_final_score(processed_data)
    
    # Output result
    print(f"Result: {final_score}")