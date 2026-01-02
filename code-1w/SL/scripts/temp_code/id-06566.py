from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    processed = []
    noise_floor = 0.02
    for reading in raw_readings:
        if abs(reading) < noise_floor:
            reading = 0.0
        processed.append(round(reading * 1000) / 1000)
    return processed

# Irrelevant helper - dead path (never called)
def legacy_calibrate(x):
    return (x + 0.1) ** 2 % 1.5

# Signal transformation with red herring operations
def transform_signal(data_seq, mode='enhanced'):
    temp_buffer = defaultdict(float)
    shifted = []
    cumulative = 0

    for i, val in enumerate(data_seq):
        temp_buffer[f'idx_{i}'] = val ** 2 + 0.1
        if i % 3 == 0:
            cumulative += math.sin(val)
        elif i % 3 == 1:
            cumulative -= math.cos(val)
        else:
            cumulative += math.tan(val + 0.1) if abs(val) > 0.1 else 0.0
        
        # Actual transformation used
        transformed_val = val * (i + 1) - cumulative
        shifted.append(abs(transformed_val))

    # Dead code: buffer never used beyond this
    stats_snapshot = dict(temp_buffer)
    normalization_factor = sum(stats_snapshot.values()) or 1.0
    for k in stats_snapshot:
        stats_snapshot[k] /= normalization_factor

    return shifted

# Decoy analysis function (misleading intermediate result)
def evaluate_coherence(pattern):
    count_pairs = Counter()
    for a, b in zip(pattern, pattern[1:]):
        key = f'{a:.1f}->{b:.1f}'
        count_pairs[key] += 1
    return sum(count_pairs.values()) % 100  # Red herring

# Core diagnostic logic with early termination
def analyze_pattern(seq, settings):
    threshold = settings['threshold']
    penalty = 0
    score = 100

    for i, x in enumerate(seq):
        if i >= len(seq) - 1:
            break
        
        diff = seq[i+1] - x
        
        # Key branching logic
        if diff > threshold:
            if x > 5:
                score += 3
            else:
                score -= 4
                penalty += 2
        elif diff < -threshold:
            if i % 4 == 0:
                score -= 1
            else:
                score += 2
        else:
            if math.isclose(diff, 0.0, abs_tol=1e-3):
                score += 1
            else:
                score -= 1

        # Early exit red herring - condition never met due to data
        if penalty > 10:
            return -999  # Dead path

    # Final adjustment using bit manipulation decoy
    magic_offset = 0
    binary_repr = bin(hash('diagnostic_v3'))
    one_bits = binary_repr.count('1')
    zero_bits = binary_repr.count('0')
    if one_bits > zero_bits:
        magic_offset = (one_bits ^ 5) & 7  # Distractor computation

    # Real final calculation
    result = (score + magic_offset) * 7
    return result

# Unused utility - string-based checksum (decoy)
def compute_tag(data):
    tag = 0
    for item in map(str, data):
        for c in item:
            tag = (tag * 31 + ord(c)) % 10007
    return tag

# Main execution flow
if __name__ == '__main__':
    # Initial sensor input
    raw_sensor_data = [0.12, -0.05, 0.34, 0.21, 0.58, -0.18, 0.43, 0.07]
    
    # Irrelevant baseline reference (distractor)
    reference_profile = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    profile_mean = sum(reference_profile) / len(reference_profile)
    
    # Preprocess actual data
    cleaned_readings = preprocess_readings(raw_sensor_data)
    
    # Transform with misleading intermediate
    transformed_data = transform_signal(cleaned_readings, mode='enhanced')
    
    # Spurious coherence check (result ignored)
    _ = evaluate_coherence(transformed_data)
    
    # Configuration with plausible but partially unused keys
    config = {
        'version': '3.1',
        'threshold': 0.5,
        'timeout_ms': 500,
        'debug_mode': False
    }
    
    # Critical statement: target variable assignment
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Output required for evaluation
    print(f"Result: {final_diagnostic}")