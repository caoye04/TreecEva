from itertools import compress, cycle

def analyze_signal_integrity(raw_samples):
    # Irrelevant preprocessing: case conversion on string artifacts
    header_tag = 'SIG_PROC_V2'
    normalized_tag = header_tag.lower().replace('_', '')
    magic_offset = sum([ord(c) for c in normalized_tag]) % 7

    # Distractor: unused transformation chain
    shifted_samples = [(x + magic_offset) * 0.97 for x in raw_samples if x > 0]
    filtered_peaks = [s for s in shifted_samples if s > 1.5]

    # Real logic: count valid pulses above noise floor
    pulse_count = 0
    for i, val in enumerate(raw_samples):
        if val >= 2.0 and i % 2 == 0:
            pulse_count += 1
    return pulse_count

def evaluate_redundancy(pattern):
    # Dead code path - never called
    cyclic = cycle([1, 0, 1])
    masked = list(compress(pattern, [p % 2 for p in pattern]))
    return len(masked)

def decode_checksum(metadata):
    # Misleading intermediate result
    temp_key = ''.join(reversed(metadata))
    checksum = 0
    for i, char in enumerate(temp_key):
        checksum += ord(char) * (i + 1)
    return checksum % 100

def compute_aggregate(log):
    base_weight = 1.0
    adjustment = 0.0
    history = []

    # Nested control flow with distractors
    for entry in log:
        tag = entry['label']
        value = entry['val']
        flag = entry['flag']

        # Real condition affecting final score
        if 'CRIT' in tag:
            if value < 50:
                adjustment -= 15.5
            else:
                adjustment += 10.2

        # Red herring: complex but irrelevant string manipulation
        padded_tag = tag.rjust(10, 'X').lstrip('X')
        shift_factor = len(padded_tag) % 3

        # Another red herring: tuple unpacking with no downstream use
        if flag:
            metadata_tuple = ('DEBUG', 42, shift_factor)
            level, code, _ = metadata_tuple
            # Unused variable 'level', 'code'

        # Real accumulation
        if value > 0:
            history.append(value * base_weight)

        # Decoy mutation
        value = max(value, 1)  # This does not affect outer scope due to pass-by-value behavior

    # Critical early return that prevents misuse of decoy paths
    if len(history) == 0:
        return -999.0

    # Real computation buried among distractions
    raw_total = sum(history)
    modifier = decode_checksum('FEEDDATA')  # Fixed output: 43
    aggregate = raw_total + adjustment + (modifier * 0.1)

    # Final transformation
    final_value = round(aggregate * 2) / 2  # Snap to nearest 0.5
    return final_value

# Main execution context
if __name__ == '__main__':
    # Simulated telemetry data
    sensor_samples = [0.1, 3.2, 0.5, 4.8, 2.1, 1.7, 5.5]
    reliability_log = [
        {'label': 'NODE_A', 'val': 67, 'flag': False},
        {'label': 'CRIT_B', 'val': 55, 'flag': True},
        {'label': 'CRIT_C', 'val': 40, 'flag': False},
        {'label': 'NODE_D', 'val': 73, 'flag': True}
    ]

    # Distractor function calls with side-effect-free returns
    pulse_diagnostic = analyze_signal_integrity(sensor_samples)
    dummy_cycle = evaluate_redundancy([1, 2, 3, 4])

    # Key assignment
    final_score = compute_aggregate(reliability_log)

    # Output target result
    print(f"Result: {final_score}")