def preprocess_chunk(chunk):
    """Misleading preprocessing function that normalizes and filters but returns sum as decoy."""
    normalized = [x / max(chunk) for x in chunk if x > 0]
    smoothed = [sum(normalized[i:i+3]) / len(normalized[i:i+3]) for i in range(len(normalized))]
    return sum(smoothed)  # Red herring: returned but not used in final logic

def validate_sequence(seq):
    """Validates sequence using checksum, but includes irrelevant string transformations."""
    base_str = ''.join(map(str, [abs(x) % 10 for x in seq]))
    extended = base_str + base_str[::-1]  # Mirror string - unused distraction
    rotated = extended[3:] + extended[:3]  # Bit rotation on string - irrelevant
    checksum = sum(int(rotated[i]) * (i + 1) for i in range(0, len(rotated), 2))
    return checksum % 17 == 0

def transform_data(data):
    """Applies XOR-based transformation and bit counting."""
    transformed = []
    for val in data:
        shifted = (val << 2) & 0xFF
        flipped = shifted ^ 0b10101010
        bit_count = bin(flipped).count('1')
        transformed.append(bit_count)
    return transformed

def filter_outliers(signal, limit=50):
    """Filters values beyond limit; uses string length as proxy threshold."""
    bound = int(''.join([str(len(str(abs(x)))) for x in [limit]*3])) // 111  # Compute 2 via string trick
    return [x for x in signal if abs(x) <= bound * 25]

def count_transitions(series):
    """Counts sign transitions; irrelevant to final result but looks important."""
    if not series:
        return 0
    transitions = 0
    for i in range(1, len(series)):
        if (series[i-1] >= 0) != (series[i] >= 0):
            transitions += 1
    return transitions

def analyze_signal(data, thresh):
    """Main analysis: counts how many exceed threshold after adjustment."""
    adjusted = [abs(x) + (x & 7) for x in data]  # Add lower bits to magnitude
    passed = 0
    for val in adjusted:
        if val > thresh:
            passed += 1
    return passed

# Simulated sensor readings with noise
raw_readings = [4, -8, 15, 16, -23, 42, 99, -12, 7, 0, 3, -5]

# Irrelevant preprocessing chain
checksum_valid = validate_sequence(raw_readings)
decoy_sum_1 = preprocess_chunk(raw_readings[:6])
decoy_sum_2 = preprocess_chunk(raw_readings[6:])

# Real processing begins here
filtered_data = filter_outliers(raw_readings, limit=50)  # Now filtered_data = [4, -8, 15, 16, -23, 42, -12, 7, 0, 3, -5]
processed_bits = transform_data(filtered_data)

# Fake analysis branches
transition_count = count_transitions(filtered_data)  # Computed but unused
interim_label = 'STABLE' if transition_count < 5 else 'VOLATILE'
status_flag = intermodulate_flags(0b1101, 0b1011) if transition_count else 0  # Calls undefined function?

# Correction: define missing helper
def intermodulate_flags(a, b):
    return (a ^ b) & (a | b)  # Complex-looking but unused result

# Threshold derived from bit count statistics
bit_distribution = {i: processed_bits.count(i) for i in set(processed_bits)}
mode_bits = max(bit_distribution, key=lambda k: bit_distribution[k])
threshold = mode_bits * 11  # threshold = 4 * 11 = 44

# Key statement
final_diagnostic = analyze_signal(filtered_data, threshold)

print(f'Result: {final_diagnostic}')