import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_data():
    return [14, 28, 42, 56, 70, 84, 98, 112, 126, 140]

# Legacy function - not actually used in current pipeline (dead code path)
def legacy_calibrate(x):
    return (x * 1.05) + 3.2

def transform_signal(value, mode='standard'):
    if mode == 'inverted':
        return int((value ** 0.5) * -1)
    else:
        return int(value // 7)

# Apply transformation with red herring logic
def process_signal_chain(raw_values):
    step_one = [transform_signal(v) for v in raw_values]
    temp_adjusted = []
    for val in step_one:
        # Distractor: temperature compensation not actually needed
        compensated = val + 2 if val > 15 else val + 0.5
        temp_adjusted.append(int(compensated))
    
    # Bit manipulation decoy - looks important but unused
    bit_shifted = []
    for x in temp_adjusted:
        shifted = (x << 2) ^ 5
        bit_shifted.append(shifted)  # computed but never used
    
    # Actual relevant transformation
    result_set = set()
    for x in temp_adjusted:
        if x % 3 == 0:
            result_set.add(x)
    return list(result_set)

# Secondary processing with misleading intermediate calculations
def filter_anomalies(data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    std_dev = variance ** 0.5
    
    # These are calculated but irrelevant to final logic
    outlier_threshold_high = mean_val + (2.5 * std_dev)
    outlier_threshold_low = mean_val - (1.8 * std_dev)
    
    # Real filtering uses simple modular arithmetic
    filtered = [x for x in data_list if x % 4 == 2]
    return filtered

# Core analysis using set operations and min/max logic
def analyze_readings(signals):
    base_set = set(signals)
    
    # Create distractor sets that look meaningful
    high_frequency_components = {x for x in signals if x > 10}
    harmonic_candidates = {x for x in signals if x % 5 == 0}
    phase_shifted_replicas = {x * 2 for x in signals}  # unused
    
    # Relevant logic chain
    candidate_pool = set()
    for s in base_set:
        if s >= 6:
            candidate_pool.add(s)
    
    # Final selection based on modular arithmetic and ordering
    sorted_candidates = sorted(candidate_pool)
    selected_indices = []
    for i, val in enumerate(sorted_candidates):
        if (val + i) % 3 == 1:
            selected_indices.append(i)
    
    # Compute diagnostic score from index positions
    score_accum = 0
    for idx in selected_indices:
        score_accum += sorted_candidates[idx] * (idx + 1)
    
    # Decoy calculation - looks like normalization but unused
    if score_accum > 0:
        normalized_score = round(score_accum / math.log(score_accum + 10), 4)
    else:
        normalized_score = 0.0
    
    # Final result derived from linear search through transformed indices
    final_value = 0
    search_array = [abs(idx - 2) for idx in selected_indices]
    for pos in range(len(search_array)):
        if search_array[pos] == 1:
            final_value += sorted_candidates[pos]  # note: subtle off-by-one trap avoided
    
    # Critical statement - this is the real answer source
    final_value += len(selected_indices) * 5
    
    return final_value

# Main execution flow
if __name__ == "__main__":
    raw_sensor_stream = fetch_sensor_data()
    processed_signals = process_signal_chain(raw_sensor_stream)
    cleaned_diagnostics = filter_anomalies(processed_signals)
    final_diagnostic = analyze_readings(cleaned_diagnostics)
    print(f"Result: {final_diagnostic}")