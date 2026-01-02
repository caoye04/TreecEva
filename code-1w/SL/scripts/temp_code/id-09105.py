from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    total_pairs = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] + sequence[j]) % 3 == 0:
                count += 1
            total_pairs += 1
    
    # Irrelevant computation - distractor
    unused_entropy = sum(x * x for x in sequence) / len(sequence) if sequence else 0
    return count

def preprocess_records(raw_data):
    filtered = [x for x in raw_data if x > 0]
    shifted = [x - 1 for x in filtered]
    
    # Dead code path - misleading
    temp_analysis = {}
    if len(shifted) > 100:
        temp_analysis['peak'] = max(shifted)
    
    # Semi-relevant transformation
    processed = [x for x in shifted if x % 2 == 0]
    return processed

def calculate_performance_metric(data_chunk):
    if not data_chunk:
        return 0
    
    # Use of dictionary operations
    stats = {
        'sum': sum(data_chunk),
        'min_val': min(data_chunk),
        'max_val': max(data_chunk)
    }
    
    # Use of itertools
    all_pairs = list(combinations(data_chunk[:5], 2)) if len(data_chunk) >= 2 else []
    pair_count = len(all_pairs)
    
    # Multiple assignments - tuple unpacking
    base_score, penalty = stats['sum'], 0
    
    # Complex conditional with short-circuit
    if stats['min_val'] < 5 and (stats['max_val'] > 20 or len(data_chunk) > 10):
        penalty = stats['min_val'] * 2
    
    # Early return based on condition
    if pair_count == 0:
        return base_score - penalty
    
    # Core logic step
    adjustment = 0
    for val in data_chunk:
        if val % 4 == 0:
            adjustment += 1

    final_score = base_score - penalty + (adjustment * 3)
    return final_score

# Main execution flow
raw_input_data = [3, 7, 2, 8, 5, 6, 9, 4, 10, 1]
intermediate_result = preprocess_records(raw_input_data)
processed_data = []
for item in intermediate_result:
    processed_data.append(item + 2)

# Additional irrelevant processing - distractor
snapshot_log = {idx: val * val for idx, val in enumerate(processed_data)}
avg_snapshot = sum(snapshot_log.values()) / len(snapshot_log) if snapshot_log else 0

# Key statement
final_score = calculate_performance_metric(processed_data)
print(f"Target result: {final_score}")