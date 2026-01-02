from itertools import combinations

def count_transitions(signal):
    transitions = 0
    for i in range(len(signal) - 1):
        if signal[i] != signal[i + 1]:
            transitions += 1
    return transitions

def generate_harmonics(base_freq, depth=3):
    # Irrelevant helper: generates frequency harmonics (not used in final result)
    return [base_freq * (i + 1) for i in range(depth)]

def filter_anomalies(data_stream):
    # Misleading processing step: removes 'outliers' but all values are within range
    threshold = sum(data_stream) / len(data_stream)
    return {x for x in data_stream if x >= threshold}

def analyze_signal_quality(active_set, pattern):
    # Core logic hidden among distractions
    matched_pairs = set(combinations(active_set, 2))
    pattern_match_count = 0
    
    for a, b in matched_pairs:
        if (a ^ b) & pattern == pattern:  # bitwise condition
            pattern_match_count += 1
    
    # Distractor: unused intermediate calculations
    avg_pair_value = sum(active_set) / len(active_set)
    transition_score = count_transitions([bin(x).count('1') for x in active_set])
    harmonic_sequence = generate_harmonics(avg_pair_value)  # Dead code path
    
    # Final computation
    stability_index = len(active_set) * pattern_match_count
    return int(stability_index - transition_score)

# Primary data inputs
raw_readings = [12, 7, 15, 3, 14]
baseline_shift = 5

# Preprocessing with red herrings
shifted_readings = [x ^ baseline_shift for x in raw_readings]
dropped_samples = [x for x in shifted_readings if x < 10]  # Unused

diagnostic_set = filter_anomalies(shifted_readings)
reference_pattern = 0b1101  # Binary mask for diagnostic check

# Key statement
final_diagnostic = analyze_signal_quality(diagnostic_set, reference_pattern)

# Output result
print(f"Result: {final_diagnostic}")