from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and calibration offsets
def fetch_raw_sensor_data():
    return [14, 17, 14, 23, 17, 23, 14, 29, 31, 17, 23, 14, 37, 43, 17]

# Irrelevant auxiliary function - dead code path (distractor)
def calculate_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Misleading preprocessing - looks important but not used in final result
def apply_calibration_bias(signal_list, bias=0.73):
    calibrated = []
    for val in signal_list:
        adjusted = val + bias * math.sin(val)
        calibrated.append(round(adjusted, 2))
    return calibrated

# Core transformation: extract primes and map to bit patterns
def filter_prime_signals(readings):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    # Extract unique primes while preserving order
    seen = set()
    primes = [x for x in readings if is_prime(x) and not (x in seen or seen.add(x))]
    return primes

# Transform prime values into frequency-weighted indices
def generate_weighted_indices(primes):
    index_map = defaultdict(int)
    for i, p in enumerate(primes):
        weight = (p % 7) * (i + 1)
        index_map[f'idx_{i}'] = weight
    return dict(index_map)

# Process signals through multiple filtering stages
def process_signal_chain(raw_data):
    # Step 1: Filter prime signals
    prime_filtered = filter_prime_signals(raw_data)
    
    # Step 2: Generate index mapping
    indices = generate_weighted_indices(prime_filtered)
    
    # Step 3: Compute derived features (some are red herrings)
    feature_set = {}
    cumulative = 0
    
    for k, v in indices.items():
        temp_val = v ** 2 - 3 * v + 2  # Quadratic transformation
        if v % 2 == 1:
            temp_val = abs(temp_val) // 2
        feature_set[k] = temp_val
        cumulative += temp_val
    
    # Dead-end computation - distractor
    avg_feature = cumulative / len(feature_set) if feature_set else 0
    
    # Hidden key: sum of all transformed odd-indexed weights
    key_sum = sum(v for i, v in enumerate(feature_set.values()) if i % 2 == 1)
    
    # Return both decoy and real data
    return {
        'diagnostics': feature_set,
        'cumulative_score': avg_feature,  # misleading
        'key_trace_sum': key_sum         # actually used later
    }

# Analyze processed readings to produce final diagnostic
def analyze_readings(processed):
    trace_sum = processed['key_trace_sum']
    diagnostics = processed['diagnostics']
    
    # Secondary transformation on diagnostics
    squared_contributions = [math.ceil(v ** 1.5) for v in diagnostics.values()]
    
    # Another distraction: unused complex structure
    summary_stats = {
        'count': len(diagnostics),
        'max_base': max(diagnostics.values()) if diagnostics else 0,
        'entropy': calculate_entropy(list(diagnostics.keys())),
        'norm': sum(s ** 2 for s in squared_contributions) ** 0.5
    }
    
    # Final computation chain
    base_value = trace_sum * 13
    adjustment = 0
    for i, sc in enumerate(squared_contributions):
        if i % 3 == 0:
            adjustment += sc % 17
    
    # Critical operation: inject adjustment only if conditions met
    if len(diagnostics) > 4:
        base_value -= adjustment
    else:
        base_value += adjustment
    
    # Final non-linear scaling
    final_diagnostic = int((base_value ** 2) / 19) - 107
    
    # Red herring print (never executed due to early return)
    if False:
        debug_dump = {"raw": diagnostics, "adj": adjustment}
        print(debug_dump)
    
    return final_diagnostic

# --- Execution Flow ---
raw_signals = fetch_raw_sensor_data()

# Apply meaningless calibration (result unused)
calibrated_noise = apply_calibration_bias(raw_signals, bias=0.73)

# Process the actual signal chain
processed_signals = process_signal_chain(raw_signals)

# Final analysis step
final_diagnostic = analyze_readings(processed_signals)

# Output the target result
print(f"Result: {final_diagnostic}")