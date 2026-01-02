import math

# Sensor simulation and diagnostic logic for environmental monitoring system
def generate_synthetic_readings():
    readings = []
    for i in range(60):
        val = (i * 7) % 19
        if i % 5 == 0:
            val = (val * 2 + 3) % 23
        readings.append(val)
    return readings

# Irrelevant helper - looks important but unused in final path
def deprecated_normalization(data):
    mean = sum(data) / len(data)
    return [math.sin(x - mean) for x in data]

# Decoy processing function - never called
def legacy_filter(seq):
    result = []
    for x in seq:
        if x > 10:
            result.append(x * 0.8)
        else:
            result.append(x * 1.1)
    return result

# Real preprocessing with distractors
def preprocess_sensors(raw_seq):
    # Apply modular transformation
    transformed = [(x ** 2 + 3 * x + 1) % 29 for x in raw_seq]
    
    # Red herring: character counting on dummy string
    metadata_tag = "sensor_v4_checksum"
    char_freq = {}
    for c in metadata_tag:
        char_freq[c] = char_freq.get(c, 0) + 1
    vowel_count = sum(1 for c in metadata_tag if c in 'aeiou')  # Unused
    
    # Another distraction: set operations that don't affect outcome
    ascii_set = set(ord(c) for c in metadata_tag)
    prime_ascii = {c for c in ascii_set if c > 1 and all(c % i != 0 for i in range(2, int(c**0.5)+1))}
    
    # Actual relevant step: reverse every third segment
    for i in range(0, len(transformed), 3):
        end = min(i+3, len(transformed))
        transformed[i:end] = reversed(transformed[i:end])
    
    # Dummy dictionary update - looks like calibration
    calibration_log = {}
    for i in range(len(transformed)):
        if transformed[i] % 4 == 0:
            calibration_log[f'entry_{i}'] = transformed[i] * 1.05
    
    return transformed

# Threshold configuration - some keys are decoys
threshold_map = {
    'critical': 25,
    'warning': 15,
    'info': 5,
    'debug': 0,  # irrelevant level
    'trace': -1  # red herring
}

# Diagnostic engine with multiple distractions
def analyze_readings(data, config):
    # Initialize various counters (some are dead ends)
    stats = {
        'high': 0, 'medium': 0, 'low': 0,
        'spike_count': 0, 'trend': 0
    }
    
    # Bit manipulation decoy
    accumulator = 0
    for x in data[:10]:
        accumulator ^= (x << 1) | (x >> 2)
    mask_result = accumulator & 0xFF  # looks important, unused
    
    # Real counting logic embedded among noise
    for value in data:
        if value > config['critical']:
            stats['high'] += 1
        elif value > config['warning']:
            stats['medium'] += 1
        elif value > config['info']:
            stats['low'] += 1
    
    # Spurious list operations
    windowed = [data[i:i+5] for i in range(0, len(data), 5)]
    avg_windows = [sum(win)/len(win) for win in windowed if len(win) == 5]
    fluctuation_score = sum(1 for i in range(1, len(avg_windows)) if abs(avg_windows[i] - avg_windows[i-1]) > 2)  # unused
    
    # String-based state tracking - misleading
    state_flags = []
    for s in ['high', 'medium', 'low']:
        if stats[s] > 10:
            state_flags.append(s.upper())
    flag_string = '|'.join(state_flags)
    
    # Critical calculation buried in middle
    base_score = stats['high'] * 7
    modifier = 0
    if stats['medium'] > stats['high'] * 2:
        modifier = -3
    elif stats['high'] > 0 and 'MEDIUM' not in flag_string:
        modifier = 5
    
    # More distractions: tuple unpacking with dummy values
    diagnostics = (base_score + modifier, 0, 0, 0)
    primary_diag, _, _, _ = diagnostics
    
    # Final red herring: complex trigonometric computation on unrelated value
    temporal_weight = sum(math.cos(i * math.pi / 17) for i in range(len(windowed)))
    adjusted = primary_diag * (1 + temporal_weight * 0.01)  # looks sophisticated, not used
    
    # ACTUAL answer
    final_diagnostic = base_score + modifier + 13
    
    # Dead code path - unreachable
    if False:
        fallback = sum(data) % 100
        final_diagnostic = fallback
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    raw_data = generate_synthetic_readings()
    processed_data = preprocess_sensors(raw_data)
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    print(f"Target result: {final_diagnostic}")