import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [i * 1.5 + 2.3 for i in range(18)]
    offset = sum([x % 2.0 for x in raw])  # Red herring: not used later
    filtered = [x for x in raw if x > 5.0]
    return filtered

# Irrelevant helper - dead code path
def calculate_baseline(data):
    avg = sum(data) / len(data)
    variance = sum([(x - avg)**2 for x in data]) / len(data)
    return math.sqrt(variance)

# Data transformation involving slicing and shifting
def transform_signal(signal):
    shifted = [signal[i] - signal[i-1] for i in range(1, len(signal))]
    padded = [0.0] + shifted
    reversed_chunk = padded[::-1][2:-2]  # Slicing red herring
    return padded  # Actual return

# Bit manipulation decoy function
def flag_compatibility(status_a, status_b):
    combined = (status_a << 2) | (status_b >> 1)
    mask = 0b1101
    return combined & mask

# Core pattern analyzer with recursion and modular arithmetic
def detect_cycle(sequence, modulus=7):
    if len(sequence) < 2:
        return 0
    remainder_chain = [int(x) % modulus for x in sequence]
    
    def recursive_check(index, path_sum):
        if index >= len(remainder_chain):
            return path_sum % modulus
        if remainder_chain[index] == 0:
            return recursive_check(index + 1, path_sum)
        return recursive_check(index + 1, path_sum + remainder_chain[index]*index)
    
    return recursive_check(0, 0)

# Main analysis function
def analyze_pattern(data, limit):
    # Multiple steps with distractors
    base_value = sum(data) / len(data)
    fluctuation = max(data) - min(data)
    
    # Dead logic branch based on impossible condition
    if len(data) < 5 and fluctuation < 1.0:
        adjustment = math.log(fluctuation)
    else:
        adjustment = 0.75  # Hardcoded override
    
    # Real computation path
    clipped = [x for x in data if x < limit]
    transformed = [math.sin(x * 0.1) for x in clipped]
    aggregate = sum(transformed)
    
    # Recursive cycle detection on processed values
    int_sequence = [int(abs(x * 10)) for x in transformed]
    cycle_score = detect_cycle(int_sequence, 13)
    
    # Decoy string operation
    serial_id = "SEN-" + "-".join([str(int(x))[-1] for x in data[:5]])
    checksum = sum(int(c) for c in serial_id if c.isdigit()) % 9  # Misleading use
    
    # Final computation - only this matters
    final_score = (aggregate * adjustment) + (cycle_score * 2.5)
    return int(final_score * 100) / 100  # Rounded result

# Orchestration with unused variables
if __name__ == "__main__":
    readings = collect_readings()                    # Real data source
    noise_floor = [x + 0.1 for x in readings]         # Unused parallel structure
    temp_reference = readings[::3]                   # Unused slice
    processed = transform_signal(readings)           # Used in real path
    
    config_flags = flag_compatibility(5, 9)        # Dead call
    baseline_rms = calculate_baseline(readings)      # Dead call
    
    threshold = 12.5
    final_diagnostic = analyze_pattern(processed, threshold)
    print(f"Target result: {final_diagnostic}")