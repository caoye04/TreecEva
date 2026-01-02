import math

# Sensor simulation and diagnostic analysis system
def generate_synthetic_readings():
    readings = []
    for i in range(60):
        val = (i * 17) % 97
        if i % 7 == 0:
            val = (val + 43) % 89
        readings.append(val)
    return readings

# Irrelevant helper - looks useful but not used in final path
def deprecated_filter(data):
    return [x for x in data if x > 25]

# Data transformation stage
def transform_signal(raw):
    transformed = []
    offset = 13
    for idx, value in enumerate(raw):
        shifted = (value + idx) % 100
        adjusted = abs(shifted - offset)
        transformed.append(adjusted)
    # Dead code branch - never executed due to loop logic
    if len(transformed) < 0:
        transformed.append(-1)
    return transformed

# Decoy function: appears related but unused
def calculate_entropy(data):
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Core processing with set operations and filtering
def process_diagnostic_frame(sequence):
    evens = {x for x in sequence if x % 2 == 0}
    odds = {x for x in sequence if x % 2 == 1}
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    
    # Intersect with prime set - key operation
    prime_matches = evens & primes  # Only even prime is 2
    
    # Misleading aggregation - not used later
    sum_odds = sum(odds)
    max_even = max(evens) if evens else 0
    
    # Actual signal: count how many values are in symmetric difference
    symm_diff = evens ^ odds
    signal_strength = len(symm_diff)  # This contributes indirectly
    
    # Add decoy list that looks important
    anomaly_flags = []
    for x in sequence:
        if x in primes and x % 5 == 0:
            anomaly_flags.append(x)
    # Never used beyond this point
    
    return list(evens), list(odds), signal_strength

# Threshold logic using set membership
def build_threshold_set(base_level):
    base_set = set()
    for i in range(5, 150, 7):
        base_set.add((i * 3) % 85)
    adjustment = {x for x in base_set if x > base_level}
    # Extra distraction
    padding = {x+1 for x in adjustment if x % 4 == 0}
    base_set.update(padding)
    return base_set

# Main analysis function - critical path
def analyze_readings(data_chunk, threshold_set):
    count_above = 0
    running_xor = 0
    temp_product = 1
    
    for val in data_chunk[10:50:3]:  # Strided slice
        if val in threshold_set:
            count_above += 1
            running_xor ^= val
        else:
            temp_product *= (val % 7 + 1)
            if temp_product > 10000:
                temp_product //= 2
    
    # Secondary check: how many unique high-frequency low-values
    low_vals = [x for x in data_chunk if x < 10]
    unique_lows = len(set(low_vals))
    
    # Red herring calculation
    avg_low = sum(low_vals) / unique_lows if unique_lows else 0
    
    # Critical dependency chain
    stage1 = count_above * 17
    stage2 = stage1 + running_xor
    stage3 = stage2 - unique_lows
    
    # Final result
    final_diagnostic = stage3 * 2  # <-- Target variable
    
    # Unused telemetry
    telemetry_snapshot = {
        'entries': len(data_chunk),
        'max_val': max(data_chunk),
        'spike_count': len([x for x in data_chunk if x > 90])
    }
    
    return final_diagnostic

# --- Execution Flow ---
raw_sensor_data = generate_synthetic_readings()
processed_signal = transform_signal(raw_sensor_data)
even_list, odd_list, strength_metric = process_diagnostic_frame(processed_signal)
threshold_set = build_threshold_set(20)

# Key statement
final_diagnostic = analyze_readings(processed_data=processed_signal, threshold_set=threshold_set)

print(f"Result: {final_diagnostic}")