import math

# Simulated sensor array diagnostics with interference

def collect_diagnostics(raw_samples):
    cumulative_offset = 0
    diagnostic_log = []
    for sample in raw_samples:
        if sample < 0:
            cumulative_offset += abs(sample) * 0.1
        elif sample > 100:
            cumulative_offset -= 5
        else:
            diagnostic_log.append(sample * 1.05)
    return diagnostic_log


def filter_anomalies(data_stream):
    anomalies = set()
    clean_data = []
    for i, val in enumerate(data_stream):
        if val != int(val) and (val * 10) % 2 == 0:
            anomalies.add(i)
        else:
            clean_data.append(int(val))
    # Irrelevant backup copy
    backup_copy = [x * 2 for x in clean_data if x % 3 == 0]
    discarded = [x for x in data_stream if x < 0]  # Dead code path
    return clean_data


def transform_sequence(seq):
    shifted = seq[2:] + seq[:2]  # Rotate left by 2
    reversed_chunk = shifted[::-1]
    # Multiple slicing operations with red herring
    mid_section = reversed_chunk[1:6]
    extended = mid_section + [math.sqrt(x) for x in seq if x > 30]
    normalized = [round(x, 2) for x in extended]
    return normalized


def compute_weighted_score(values):
    weights = [0.1, 0.2, 0.3, 0.4, 0.5]
    score = 0.0
    for i in range(len(values)):
        score += values[i % len(values)] * weights[i % len(weights)]
    adjustment = sum([1 for x in values if x > 25]) * 0.05
    score += adjustment  # Minor tweak
    return score


def analyze_readings(data, criteria):
    base_sum = sum(data)
    criterion_match = [x for x in data if x in criteria]
    mismatch_count = len(data) - len(criterion_match)
    # Heavily distracted logic with decoy computations
    temp_analysis = {
        'peak': max(data),
        'trough': min(data),
        'range': max(data) - min(data),
        'entropy': len(set(data)) / len(data) if data else 0
    }
    entropy_flag = temp_analysis['entropy'] > 0.7
    dummy_map = {i: math.log(1 + i) for i in range(1, 10)}  # Unused mapping
    # Critical computation buried in noise
    if entropy_flag:
        modifier = len(criterion_match) * 1.5
    else:
        modifier = len(criterion_match) * 2.0
    
    # Decoy recursive function (never called)
    def recursive_decay(n, acc=1.0):
        if n <= 1:
            return acc
        return recursive_decay(n-1, acc * 0.9)
    
    # Final result obscured by irrelevant blocks
    debug_snapshot = data[::2]  # Every second element
    outlier_ratio = sum(1 for x in data if x > 50) / len(data)
    scaling_factor = 1 + (outlier_ratio * modifier)
    final_diagnostic = int((base_sum / (mismatch_count + 1)) * scaling_factor)
    return final_diagnostic

# Main execution with multiple distractions
if __name__ == '__main__':
    raw_input_stream = [12, 34, -5, 67, 105, 23, 89, 44, 78, 31, 92]
    config_thresholds = {12, 23, 31, 44, 67, 78, 89, 92}
    metadata_cache = {'version': '2.1', 'mode': 'diagnostic'}  # Unused
    processing_mode = 'advanced'
    
    # Step 1: Collect diagnostics
    preliminary_results = collect_diagnostics(raw_input_stream)
    
    # Step 2: Filter anomalies
    filtered_output = filter_anomalies(preliminary_results)
    
    # Step 3: Transform sequence
    transformed_block = transform_sequence(filtered_output)
    
    # Step 4: Compute weighted score (distractor)
    performance_score = compute_weighted_score(transformed_block)
    
    # Step 5: Analyze readings — key step
    processed_data = [int(x) for x in transformed_block if x.is_integer() or x > 10]
    threshold_set = config_thresholds
    final_diagnostic = analyze_readings(processed_data, threshold_set)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")