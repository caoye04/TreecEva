import itertools

# Simulated sensor fusion system for environmental anomaly detection
def collect_sensor_data(baseline, threshold_multiplier=1.85):
    raw_readings = [baseline * (i + 1) ** 0.5 for i in range(7)]
    filtered = [r for r in raw_readings if r > baseline * threshold_multiplier]
    return filtered


def generate_harmonic_sequence(length, base_freq=3):
    # Irrelevant harmonic sequence generator (dead-end function)
    return [base_freq * (2 ** (n // 12)) for n in range(length)]


def shift_cipher(text, shift=3):
    # Distractor: string manipulation unrelated to main logic
    shifted = ''.join(chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.isalpha() else c for c in text.lower())
    return shifted


def extract_features(data_stream):
    magnitude = sum(d ** 2 for d in data_stream) ** 0.5
    variance = sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream) / len(data_stream)
    peak_to_avg = max(data_stream) / (sum(data_stream) / len(data_stream))
    return {'mag': magnitude, 'var': variance, 'ratio': peak_to_avg}


def compute_checksum(elements):
    # Used in one branch but not the critical path
    chk = 0
    for e in elements:
        chk = (chk * 31 + int(e)) % 10007
    return chk


def build_lookup_table(keys, default_val=1):
    # Creates unused mapping (red herring)
    table = {k: default_val for k in keys}
    for k in table:
        table[k] += len(str(k))
    return table


def detect_anomaly_patterns(signal_list):
    if len(signal_list) < 4:
        return [False, True, False]
    
    # Real pattern detection
    diffs = [signal_list[i+1] - signal_list[i] for i in range(len(signal_list)-1)]
    product_chain = 1
    for d in diffs[:3]:
        product_chain *= abs(d) + 1
    
    # Decoy intermediate
    temp_score = sum(diffs) * 0.987
    
    result_flags = [
        product_chain > 50,
        diffs[0] < diffs[-1],
        len(diffs) % 2 == 0
    ]
    
    return result_flags


def recursive_blend(value, depth):
    if depth <= 0 or value > 1000:
        return value % 7
    return recursive_blend(value * 2 + depth, depth - 1)


def analyze_pattern(signals, key):
    # Core analysis logic
    features = extract_features(signals)
    pattern_flags = detect_anomaly_patterns(signals)
    
    # Irrelevant string processing distraction
    encoded_key = shift_cipher(key, len(signals) % 5)
    key_value = sum(ord(c) for c in encoded_key) % 100
    
    # Meaningless set operations
    unique_mags = set()
    for _ in range(2):
        unique_mags.add(int(features['mag']))
        unique_mags.add(int(features['var'] * 10))
    
    # Critical computation chain
    base = int(features['mag'])
    adjustment = features['ratio'] * 100
    if pattern_flags[0] and not pattern_flags[2]:
        adjustment -= 15
    elif pattern_flags[1]:
        adjustment += 22
    
    intermediate = base + int(adjustment)
    
    # Redundant dictionary transformation
    diagnostics = {
        'level_1': base,
        'level_2': int(features['var']),
        'level_3': intermediate
    }
    
    final_diagnostic = intermediate
    
    # Dead code path with confusing recursion
    if key_value < 0:
        for i in range(3):
            final_diagnostic = recursive_blend(final_diagnostic, 3)
    
    # Unused itertools combination
    combinations = list(itertools.combinations_with_replacement([1,2], 2))
    combo_sum = sum(sum(c) for c in combinations)  # Computed but unused
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Sensor baseline simulation
    baseline_input = 12.5
    collected_signals = collect_sensor_data(baseline_input, threshold_multiplier=1.85)
    
    # Irrelevant data structure setup
    harmonic_series = generate_harmonic_sequence(10, base_freq=7)
    lookup = build_lookup_table(harmonic_series, default_val=2)
    checksum = compute_checksum([int(s) for s in collected_signals])
    
    # System key with string properties
    system_key = 'quantum-flux'
    
    # Actual critical computation
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Output required result
    print(f"Result: {final_diagnostic}")