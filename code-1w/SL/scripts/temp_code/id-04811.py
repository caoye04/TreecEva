import math

# Simulated sensor array diagnostics with signal transformation and noise filtering
def preprocess_signal(raw_readings):
    filtered = []
    noise_floor = 0.05
    gain_boost = 1.7
    temp_accum = 0

    for val in raw_readings:
        if abs(val) < noise_floor:
            continue
        boosted = val * gain_boost
        temp_accum += boosted
        if temp_accum > 10.0:
            temp_accum = 0
        filtered.append(round(boosted, 3))

    # Irrelevant transformation
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return filtered

# Legacy function - unused but looks relevant
def legacy_process(data):
    return [math.sin(x) for x in data]

# Signal transformer with bit manipulation red herring
def encode_timing(signal):
    encoded = []
    base_shift = 3
    magic_mask = 0b1101
    timing_log = []  # Unused variable

    for i, x in enumerate(signal):
        shifted = int(abs(x) * 100) << base_shift
        masked = shifted & magic_mask
        encoded.append(shifted | i)  # Use of bitwise OR
    
    # Dead code path
    if len(encoded) > 100:
        return [x ^ 0xFF for x in encoded]
    return encoded

# Core analysis with conditional logic and set operations
def analyze_signal(encoded_values, thresh):
    valid_set = set()
    invalid_set = set()
    rolling_sum = 0
    cycle_marker = 0
    result_flags = []

    for idx, v in enumerate(encoded_values):
        if v == 0:
            continue
        
        # Conditional expression distraction
        flag_state = 'valid' if (v % 2 == 1) and (v > 100) else 'invalid'
        
        # Set-based filtering that actually matters
        if v % 4 == 0 and v % 6 != 0:
            valid_set.add(v)
        elif v > 2000:
            invalid_set.add(v)
        
        rolling_sum += v
        
        # Early break red herring
        if rolling_sum > 50000:
            cycle_marker = idx
            break
    
    # Real computation path
    active_count = len(valid_set)
    suppression_factor = 0.85 if len(invalid_set) > 0 else 1.0
    
    # Final diagnostic uses modular arithmetic and combinatorics
    combinations = 1
    n = active_count
    r = 2
    if n >= r:
        combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    
    # Key calculation
    base_score = rolling_sum % 971
    final_diagnostic = int((base_score * suppression_factor) + combinations)
    
    # Decoy variables and string methods that do nothing
    log_entry = f"Analysis complete: {final_diagnostic} units detected"
    log_entry.upper().replace(" ", "_").strip()
    
    return final_diagnostic

# Unused helper functions to increase interference
def validate_checksum(data):
    return sum(data) % 256

def generate_report(snapshot):
    return {"status": "archived", "data_length": len(snapshot)}

# Main execution flow
if __name__ == "__main__":
    # Simulated input - deterministic
    sensor_input = [0.1, -0.3, 0.04, 0.8, -1.2, 2.5, 0.03, -0.9, 1.7, 3.4, 0.2]
    
    # Multi-step transformation chain
    cleaned = preprocess_signal(sensor_input)
    transformed_data = encode_timing(cleaned)
    threshold = len(transformed_data) * 0.5
    
    # Critical statement
    final_diagnostic = analyze_signal(transformed_data, threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")