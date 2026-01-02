def analyze_pattern(sequence):
    # Irrelevant helper that is never called
    return sum(1 for c in sequence if c.isupper())

# Decoy configuration constants (distractors)
MAX_ITERATIONS = 15000
BASE_OFFSET = 37
RECALIBRATION_FACTOR = 0.89
TIMEOUT_BUFFER = 240

# Real data structures with mixed relevance
threshold_map = {
    'alpha': 42,
    'beta': 17,
    'gamma': 8,
    'delta': 23
}

sensor_data = [
    {'type': 'alpha', 'signal': 86, 'checksum': 'A1'},
    {'type': 'beta', 'signal': 35, 'checksum': 'B2'},
    {'type': 'gamma', 'signal': 19, 'checksum': 'C3'},
    {'type': 'alpha', 'signal': 41, 'checksum': 'A4'},
    {'type': 'delta', 'signal': 47, 'checksum': 'D5'},
    {'type': 'gamma', 'signal': 14, 'checksum': 'C6'}
]

# Unused but plausible-looking processing functions (dead code path)
def validate_checksum(tag):
    if len(tag) != 2:
        return False
    return tag[0] in 'ABCDE' and tag[1].isdigit()

def encrypt_signal(value, key=7):
    # Bit manipulation red herring
    return (value ^ key) << 2

# Main processing function with embedded logic chain
def process_readings(data, thresholds):
    cumulative_score = 0
    anomaly_count = 0  # Distractor: used only in debug logs
    temp_buffer = []   # Distractor: collects unused intermediates

    for entry in data:
        sensor_type = entry['type']
        signal_value = entry['signal']
        
        # Real logic begins: apply modular arithmetic filter
        if signal_value % 5 == 0:
            continue  # Skip round multiples (real filtering rule)

        base_threshold = thresholds.get(sensor_type, 0)
        
        # Real conditional branch with bitwise twist
        if signal_value > base_threshold:
            # Score gain: XOR-based transformation
            adjusted = (signal_value & 0xFF) ^ 0x5A  # Bitwise operation
            cumulative_score += adjusted % 100
        else:
            # Anomaly path (never triggered in this dataset)
            anomaly_count += 1
            temp_buffer.append(signal_value)

        # Additional logic: case conversion on checksum (string method distractor)
        raw_tag = entry['checksum']
        upper_tag = raw_tag.upper()  # Use of string method (irrelevant)
        lower_tag = raw_tag.lower()
        char_sum = sum(ord(c) for c in upper_tag)  # Meaningless computation
        temp_buffer.append(char_sum)  # Feeds decoy buffer

        # Early termination red herring (condition never met)
        if len(temp_buffer) > 10:
            cumulative_score = -1
            break

    # Final transformation chain (critical path)
    final_diagnostic = cumulative_score
    final_diagnostic = (final_diagnostic * 3) + 7
    final_diagnostic = final_diagnostic ^ 0xBEEF  # Final XOR mask
    final_diagnostic = abs(final_diagnostic) % 100000  # Bound result

    return final_diagnostic

# Debug probe - looks important but unused in logic
consistency_check = sum(threshold_map.values()) * 2 - 44

# Trigger execution
diagnostic_log = []
final_diagnostic = process_readings(sensor_data, threshold_map)
diagnostic_log.append(f"Final: {final_diagnostic}")

# Output result as required
print(f"Result: {final_diagnostic}")