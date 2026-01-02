import math

# Simulated sensor array data from a distributed monitoring system
def acquire_signals():
    raw_readings = [127, 255, 192, 64, 95, 131]
    timestamps = [1638420000, 1638420060, 1638420120, 1638420180, 1638420240, 1638420300]
    return list(zip(raw_readings, timestamps))

# Filter out signals below threshold (distractor: not actually used in final path)
def filter_noisy(data, thresh=100):
    return [x for x in data if x[0] > thresh]

# Transform signal using bitwise obfuscation (unused red herring)
def obfuscate_signal(val):
    shifted = (val << 3) & 0xFF
    return shifted ^ 0xAA

# Core processing: extract and normalize signal magnitudes
def extract_magnitudes(signal_data):
    extracted = []
    for reading, ts in signal_data:
        # Normalize via logarithmic scale and apply phase shift
        if reading > 0:
            normalized = math.log(reading, 2)
            adjusted = normalized * (ts % 5)  # artificial modulation
            extracted.append(int(adjusted))
    return extracted

# Apply checksum validation (distractor function - never called)
def validate_checksum(arr):
    checksum = 0
    for val in arr:
        checksum = (checksum + val) % 256
    return checksum == 0

# Process each magnitude with bit manipulation and conditional logic
def process_magnitude(val):
    if val <= 0:
        return val + 5
    
    # Bitwise transformation chain
    step_a = val ^ 0xF
    step_b = step_a >> 2
    step_c = step_b | 0x15
    
    # Introduce conditional flip based on parity
    if bin(step_c).count('1') % 2 == 0:
        step_c = ~step_c & 0xFF  # invert bits if even hamming weight
    
    # Distractor computation (assigned but unused)
    decoy_result = (step_c * 3) + 7
    
    return step_c

# Wrapper to map processing across all magnitudes
def process_all(mags):
    results = []    
    indices = []
    
    # Use enumerate to track positions (some are ignored)
    for i, mag in enumerate(mags):
        processed = process_magnitude(mag)
        results.append(processed)
        
        # Dead code branch: condition never met due to data range
        if i > len(mags) * 10:
            indices.append(i)
    
    # Misleading intermediate aggregate (not used later)
    temp_avg = sum(results) / len(results) if results else 0
    temp_flag = temp_avg > 20
    
    return results

# Aggregate processed values using XOR folding (key operation)
def aggregate_measures(values):
    if not values:
        return 0
    
    accumulator = values[0]
    for i in range(1, len(values)):
        accumulator ^= values[i]  # XOR fold all
    
    # Additional transformation: add length as salt
    final_hash = accumulator + len(values)
    
    # Decoy statistical measures (computed but irrelevant)
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    deviation_score = math.sqrt(variance) if variance > 0 else 0
    
    return final_hash

# Unused auxiliary diagnostic (dead function)
def generate_health_report(data):
    active_nodes = len(data)
    status_flags = [1 if x > 50 else 0 for x in data]
    return {'nodes': active_nodes, 'integrity': sum(status_flags)}

# Entry point simulation
if __name__ == "__main__":
    # Acquire raw sensor signals
    signal_bundle = acquire_signals()
    
    # Extract magnitude components (critical path start)
    raw_magnitudes = extract_magnitudes(signal_bundle)
    
    # Distractor: filtered set (computed but unused)
    high_freq_signals = filter_noisy(signal_bundle, thresh=128)
    hf_mags = extract_magnitudes(high_freq_signals)
    
    # Process all valid magnitudes
    processed_signals = process_all(raw_magnitudes)
    
    # Final diagnostic computation (target execution point)
    final_diagnostic = aggregate_measures(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")