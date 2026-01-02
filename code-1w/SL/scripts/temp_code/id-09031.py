def analyze_signal_pattern(data, mode='basic'):
    """Irrelevant signal analysis function (dead code path)"""
    if mode == 'advanced':
        return [x * 2 for x in data if x > 5]
    return [x for x in data if x % 2 == 0]


def decode_transmission(stream):
    """Unused transmission decoder (distractor)"""
    return ''.join(chr(x % 97 + 97) for x in stream[:10])


def validate_phase_integrity(phase_vector):
    """Misleading integrity check with side computation"""
    checksum = sum(p ** 2 for p in phase_vector) % 1000
    deviation = max(phase_vector) - min(phase_vector)
    # This looks important but isn't used later
    return checksum < 500 and deviation < 200


def compute_entropy(sequence):
    """Red herring entropy calculation"""
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = sum(-f/total * log(f/total) for f in freq.values())
    return round(entropy, 4)


def calculate_thermal_output(readings, filter_fn):
    """Core function that computes the actual answer"""
    filtered = [r for r in readings if filter_fn(r)]
    
    # Intermediate transformation with distractors
    scaled = [abs(r * 1.5) for r in filtered]
    offset = len([x for x in scaled if x > 10])  # Looks important
    
    # Real computation chain
    processed = []
    for i, val in enumerate(scaled):
        if i % 2 == 0:
            processed.append(val + i)
        else:
            processed.append(val - i//2)
    
    # Accumulation with conditional expression
    accumulator = 0
    for p in processed:
        accumulator += p if p > 7 else (p ** 2)  # Conditional logic

    # Final adjustment using slicing and min/max
    window = processed[-5:]  # Last 5 elements
    adjustment = min(window) * 0.5 if len(window) >= 3 else max(window) * 0.1
    result = accumulator - adjustment
    
    # Irrelevant bit manipulation (looks sophisticated)
    binary_shift = int(result) << 2 >> 1
    parity_check = bin(binary_shift).count('1') % 2
    
    # Return final thermal capacity
    return int(result)

# Main execution block
if __name__ == '__main__':
    # Initialize various data structures (many are distractions)
    sensor_readings = [3, 7, -2, 8, 12, 5, 9, 4, 11, 6]
    calibration_sequence = [1.1, 2.3, 1.9, 3.4, 2.2]
    protocol_flags = [True, False, True, True, False]
    energy_sequence = [x * 2 + 1 for x in range(8)]  # [1,3,5,...,15]

    # Unused transformations
    encoded_stream = [ord(c) % 50 for c in 'quantum_protocol']
    phase_data = [i**2 - 3*i for i in range(1, 7)]

    # Threshold filter (used in main calculation)
    threshold_filter = lambda x: x > 4

    # Dead code assignments (red herrings)
    system_health = sum(protocol_flags)
    baseline_reference = sum(calibration_sequence) / len(calibration_sequence)
    signal_strength = max(sensor_readings) - min(sensor_readings)

    # Key computation involving multiple concepts
    thermal_capacity = calculate_thermal_output(energy_sequence, threshold_filter)
    
    # Print required result
    print(f"Result: {thermal_capacity}")