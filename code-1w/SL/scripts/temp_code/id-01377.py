def analyze_pattern(sequence, threshold):
    count = 0
    temp_sum = 0
    for i in range(len(sequence)):
        if sequence[i] > threshold:
            count += 1
            temp_sum += sequence[i]
    return count, temp_sum


def extract_features(data_slice):
    # Irrelevant feature extraction (distractor)
    mean_val = sum(data_slice) / len(data_slice)
    variance = sum((x - mean_val) ** 2 for x in data_slice) / len(data_slice)
    peak = max(data_slice)
    return {'mean': mean_val, 'variance': variance, 'peak': peak}


def evaluate_performance(results, base):
    adjusted_base = base * 1.5
    bonus_factor = 0
    penalty = 0

    # Real logic begins
    valid_entries = [r for r in results if r >= base]
    
    # Distractor: unused transformation
    inverted = [100 - x for x in results if x < 50]
    
    if len(valid_entries) >= 3:
        bonus_factor = 2
    else:
        penalty = 5

    # Use slicing to get middle segment
    mid_segment = results[1:-1]
    high_performers = [x for x in mid_segment if x > adjusted_base]

    # Another distractor variable
    avg_mid = sum(mid_segment) / len(mid_segment) if mid_segment else 0

    # Core scoring logic
    raw_score = sum(valid_entries)
    adjustment = len(high_performers) * bonus_factor - penalty
    final_score = raw_score + adjustment

    # Additional irrelevant computation
    bit_analysis = len(valid_entries) ^ len(high_performers)
    checksum = sum(results) % 7

    return final_score

# Main execution
base_threshold = 42
raw_data = [38, 45, 67, 41, 73, 52, 39]

# Distractor: auxiliary analysis
pattern_stats = analyze_pattern(raw_data, base_threshold)
features = extract_features(raw_data[::2])  # Every other element

# Key processing step
task_results = [x + (x % 4) for x in raw_data]

# Critical statement where answer is determined
final_score = evaluate_performance(task_results, base_threshold)

print(f"Result: {final_score}")