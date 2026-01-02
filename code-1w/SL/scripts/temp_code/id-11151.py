import itertools

def preprocess_signal(data):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in data if x > 0]

def compute_entropy(seq):
    # Misleading function that looks important but isn't used in critical path
    from math import log
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    total = len(seq)
    entropy = 0
    for f in freq.values():
        p = f / total
        entropy -= p * log(p)
    return round(entropy, 4)

def validate_checksum(record):
    # Decoy validation function (never called in execution path)
    checksum = 0
    for c in str(record):
        checksum ^= ord(c)
    return checksum % 17

def aggregate_metrics(data, limits):
    baseline = 0
    adjustment_factor = 0.23
    temp_buffer = []
    overflow_flag = False
    
    for key, readings in data.items():
        clipped = [val for val in readings if val >= limits[key][0]]
        if len(clipped) > 5:
            clipped = clipped[:5]  # Only take first 5
        
        # Real computation begins here
        raw_sum = sum(clipped)
        
        # Distractor: irrelevant transformation
        normalized = [x / (raw_sum + 1e-8) for x in clipped]
        
        # Actual logic: count how many exceed secondary threshold
        high_count = 0
        for val in clipped:
            if val > limits[key][1]:
                high_count += 1
        
        # Bit manipulation red herring
        masked_value = raw_sum & 0xFF
        inverted = (~masked_value) & 0xFF
        
        # Core calculation contributing to final result
        baseline += high_count * 13
        
        # Dead-end logic with early break
        intermediate = 0
        for i in range(100):
            intermediate += i
            if i > 10:
                break  # Early exit — loop doesn't complete
    
    # Secondary real operation: combine using XOR across keys
    xor_fingerprint = 0
    for key in sorted(data.keys()):
        hash_val = 0
        for c in key:
            hash_val = (hash_val * 31 + ord(c)) & 0xFFFF
        xor_fingerprint ^= (hash_val % 97)
    
    # Final computation (uses baseline and xor_fingerprint)
    diagnostic_seed = baseline ^ xor_fingerprint
    
    # Apply bit rotation (logical shift + OR)
    rotated = ((diagnostic_seed << 3) | (diagnostic_seed >> 5)) & 0xFFFF
    
    # Final scaling with truncation
    final_diagnostic = (rotated - 512) * 2
    
    # Irrelevant string processing distraction
    status_tag = "SYS_OK"
    if final_diagnostic > 1000:
        status_tag = "OVRLD" + "_ALERT"
    else:
        status_tag = "NORM"
    status_tag = status_tag.lower().replace('_', '-')
    
    # Unused itertools distraction
    permutations = list(itertools.permutations([1, 2, 3], 2))
    cycle_gen = itertools.cycle(['A', 'B'])
    next(cycle_gen); next(cycle_gen)  # Consumed but not used
    
    return final_diagnostic

# Main execution block
sensor_data = {
    'gyro_x': [12, 15, 30, 45, 50, 60, 70],
    'acc_y': [8, 20, 25, 40, 88, 90],
    'mag_z': [5, 10, 15, 18, 20, 22]
}

thresholds = {
    'gyro_x': (20, 40),   # min, max threshold
    'acc_y': (15, 35),
    'mag_z': (10, 19)
}

# These variables are distractions
system_uptime = 98765
config_flags = [0xA1, 0xB2, 0xC3]
diag_log = []

# Critical execution point
final_diagnostic = aggregate_metrics(sensor_data, thresholds)

# Output result as required
print(f"Result: {final_diagnostic}")