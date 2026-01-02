import itertools

# Simulated sensor array diagnostics with noise and redundant data
def analyze_sensor_stream(raw_readings, threshold_multiplier=1.3):
    base_reference = 42
    temp_cache = []
    cumulative_shift = 0
    diagnostic_log = []
    
    for i, entry in enumerate(raw_readings):
        if i % 7 == 0:
            # Red herring: rarely used reset logic
            cumulative_shift = (cumulative_shift + base_reference) % 19
        
        # Real signal extraction: only entries with even index and high magnitude
        if i % 2 == 0 and abs(entry) > 50:
            adjusted = entry // (i + 1) if i > 0 else entry
            temp_cache.append(adjusted)
    
    # Decoy transformation: looks important but unused later
    decoy_aggregate = sum(x ** 0.5 for x in temp_cache if x > 0) * threshold_multiplier
    
    # Actual filtering path
    filtered_signal = [x for x in temp_cache if x % 4 == 3]
    
    # Inject phantom values that get removed later
    extended_buffer = filtered_signal + [-999, -888, -777]
    cleaned = [x for x in extended_buffer if x != -999]  # Remove one decoy
    final_clean = list(itertools.filterfalse(lambda x: x in [-888, -777], cleaned))  # Remove remaining decoys
    
    # Log generation (distraction)
    for val in final_clean:
        if val < 0:
            diagnostic_log.append(f"ERR_{abs(val)}")
        else:
            diagnostic_log.append(f"OK_{val}")
    
    return final_clean, diagnostic_log

def validate_checksum(sequence, mode='strict'):
    # Unused validation function - dead code path
    if mode == 'relaxed':
        return sum(sequence) % 11
    return sum(x * x for x in sequence) % 23

def compute_entropy(signal):
    # Misleading advanced analysis - not used in main flow
    from math import log2
    total = sum(abs(x) for x in signal)
    if total == 0:
        return 0.0
    probs = [abs(x) / total for x in signal]
    return -sum(p * log2(p) for p in probs if p > 0)

def process_diagnostics(data_list, offset):
    # Core calculation: modular arithmetic with offset accumulation
    running_total = 0
    for j, val in enumerate(data_list):
        if j % 3 == 0:
            running_total += val * offset
        elif j % 3 == 1:
            running_total += (val + offset) % 7
        else:
            running_total -= (val % 5)
    
    # Secondary adjustment using bit manipulation
    mask = 0b1101
    masked_effect = (running_total & mask) ^ 0b1010
    
    # Final composition
    result = (running_total + masked_effect) // 3
    return result

# Main execution block
if __name__ == "__main__":
    # Simulated input - appears noisy and complex
    sensor_input = [150, -30, 200, 45, -170, 60, 220, -80, 190, 35, -210, 70, 240]
    
    # Initial processing
    filtered_data, logs = analyze_sensor_stream(sensor_input, threshold_multiplier=1.3)
    
    # Irrelevant entropy check (computationally heavy but unused)
    _ = compute_entropy(sensor_input)
    
    # Key control variable - derived from fixed reference
    base_offset = (42 * 2) % 17
    
    # Dead code: checksum validation never called
    # checksum = validate_checksum(filtered_data)
    
    # Critical statement
    final_diagnostic = process_diagnostics(filtered_data, base_offset)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")