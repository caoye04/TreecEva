import math

# System diagnostics module (simulated)
def collect_metrics(data_points):
    # Irrelevant function: collects metrics but not used in final result
    stats = {}
    stats['max'] = max(data_points)
    stats['min'] = min(data_points)
    stats['range'] = stats['max'] - stats['min']
    stats['mid'] = (stats['max'] + stats['min']) / 2
    return stats

def preprocess_signal(signal_stream):
    # Distractor function: performs transformation but unused in critical path
    normalized = [x / max(signal_stream) for x in signal_stream]
    filtered = [x for x in normalized if x > 0.1]
    return [int(x * 100) for x in filtered]

def generate_basis(n):
    # Dead code path: generates number basis but never called
    return {i: (i ** 2) % n for i in range(1, n)}

def compute_entropy(values):
    # Misleading intermediate: computes entropy but not used in answer
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def extract_features(raw_data):
    # Complex distractor with multiple layers
    feature_set = set()
    for item in raw_data:
        if item % 3 == 0:
            feature_set.add(item * 2)
        elif item % 5 == 0:
            feature_set.add(item + 10)
    # Additional red herring operations
    temp_cache = [x for x in feature_set if x < 100]
    temp_cache.sort(reverse=True)
    return feature_set

def encode_sequence(seq, key_offset=7):
    # Core relevant function (partially)
    encoded = []
    shift = key_offset * 2
    for val in seq:
        transformed = (val ^ shift) + 1
        encoded.append(transformed)
    return encoded

def build_reference_map(keys):
    # Generates a map used later in analysis
    ref_map = {}
    for k in keys:
        ref_map[k] = (k % 4, (k * 3) % 7, k > 50)
    return ref_map

def analyze_patterns(seq, ref_map):
    # Critical function containing key logic steps
    state_flags = [False, True, False]
    accumulator = 0
    
    # Step 1: Filter sequence using bit condition
    candidates = [x for x in seq if (x & 5) == 1]
    
    # Step 2: Map to reference-derived categories
    category_count = {0: 0, 1: 0, 2: 0}
    for c in candidates:
        if c in ref_map:
            cat = ref_map[c][1]  # Use second tuple element as category
            if cat in category_count:
                category_count[cat] += 1
            else:
                category_count[2] += 1  # default
    
    # Step 3: Apply combinatoric weight based on counts
    weighted_sum = 0
    for idx, cnt in enumerate(category_count.values()):
        combinations = math.comb(cnt + 2, 2) if cnt >= 0 else 0  # C(n+2,2)
        weighted_sum += combinations * (idx + 1)
    
    # Step 4: Conditional adjustment via boolean logic chain
    flag_condition = (category_count[1] > 1) and (weighted_sum % 2 == 1)
    if any(state_flags) or flag_condition:
        accumulator += weighted_sum * 3
    else:
        accumulator += weighted_sum * 2
    
    # Step 5: Final adjustment using arithmetic chain
    accumulator = (accumulator + 7) // 5
    accumulator = accumulator * accumulator  # square
    return accumulator

# --- Main execution block ---
if __name__ == "__main__":
    # Input data (real system telemetry)
    sensor_readings = [12, 24, 35, 46, 58, 63, 72, 81, 94, 105]
    
    # Irrelevant preprocessing (distractor)
    metrics = collect_metrics(sensor_readings)
    processed_signal = preprocess_signal(sensor_readings)
    
    # Unused feature extraction (red herring)
    features = extract_features(sensor_readings)
    
    # Generate basis structure (dead code call avoided)
    # basis = generate_basis(10)  # never invoked
    
    # Compute misleading metric
    entropy = compute_entropy(sensor_readings)  # not used later
    
    # --- Core computation chain ---
    encoded_sequence = encode_sequence(sensor_readings, key_offset=6)
    
    # Build reference map from subset of original data
    active_keys = [x for x in sensor_readings if x % 3 == 0]  # multiples of 3
    reference_map = build_reference_map(active_keys)
    
    # Key statement: this determines the final answer
    final_diagnostic = analyze_patterns(encoded_sequence, reference_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")