def analyze_pattern(sequence, threshold):
    if len(sequence) < threshold:
        return sum(x ** 0.5 for x in sequence if x > 0)
    return sum(x * 2 for x in sequence if x % 2 == 0)


def validate_signal(strength, noise_level=0.1):
    adjusted = strength * (1 - noise_level)
    tolerance = 5.0
    return int(adjusted // tolerance)


def transform_coordinates(coords):
    # Irrelevant geometric transformation (dead logic path)
    x, y = coords
    rotated_x = x * 0.866 - y * 0.5
    rotated_y = x * 0.5 + y * 0.866
    return (rotated_x, rotated_y)


def compute_entropy(data):
    # Distractor function: looks important but unused
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)


def integrate_readings(raw_values, mode='fast'):
    accumulator = 0
    temp_buffer = []
    for val in raw_values:
        if val < 0:
            continue
        if mode == 'precise':
            accumulator += val ** 0.5
        else:
            accumulator += val // 3
        temp_buffer.append(accumulator)
    
    # Dead code branch: never executed due to fixed mode
    if mode == 'debug':
        print(f"Tracing: {temp_buffer}")
        
    return accumulator


def process_readings(data, factor):
    # Core relevant logic begins
    base_score = 0
    
    # Extract and filter sensor values
    filtered = [x for x in data if x > 10 and x < 100]
    
    # Bit manipulation red herring
    mask = 0b1101
    masked_values = [x & mask for x in filtered]
    
    # Conditional expression used
    offset = 7 if sum(masked_values) > 50 else 3
    
    # Accumulate with conditional logic
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            base_score += val // factor
        else:
            base_score -= val % factor
    
    # Secondary transformation with tuple unpacking
    stats = (min(filtered), max(filtered), len(filtered))
    min_val, max_val, count = stats
    
    # Decoy calculation (looks like normalization)
    fake_norm = (base_score + min_val) / (max_val + 1)
    
    # Real contribution: bitwise XOR chain
    checksum = 0
    for v in filtered[::2]:
        checksum ^= v
    
    # Final composition
    intermediate = base_score + checksum
    final_diagnostic = abs(intermediate - offset)  # Key assignment point
    
    # Unused branching distraction
    if final_diagnostic > 1000:
        fallback = integrate_readings(data, mode='precise')
        final_diagnostic = fallback // 10
    
    return final_diagnostic

# Main execution
sensor_data = [15, 22, 8, 95, 12, 64, 33, 41, 7, 55]
calibration_factor = 4

# Irrelevant coordinate test
coords = (10, 20)
transformed = transform_coordinates(coords)

# Unused validation call
signal_code = validate_signal(87)

# Spurious pattern analysis
pattern_result = analyze_pattern(sensor_data, 8)

# Critical statement
final_diagnostic = process_readings(sensor_data, calibration_factor)

# Output result
print(f"Result: {final_diagnostic}")