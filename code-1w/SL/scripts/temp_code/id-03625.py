from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def analyze_readings(data_stream):
    readings_count = defaultdict(int)
    total_energy = 0.0
    peak_magnitude = -float('inf')
    null_count = 0

    for val in data_stream:
        readings_count[val] += 1
        if val == 0:
            null_count += 1
        else:
            total_energy += math.log(abs(val) + 1e-5)
            if val > peak_magnitude:
                peak_magnitude = val

    # Irrelevant aggregation
    entropy = 0.0
    for count in readings_count.values():
        p = count / len(data_stream)
        entropy -= p * math.log2(p)

    return total_energy, peak_magnitude, entropy

# Distractor function - never called
def legacy_compatibility_mode(x):
    shift_key = 7
    result = 0
    for i in range(8):
        result ^= (x >> i) & 1
        result = (result << 1) | ((x >> i) & 1)
    return result % 97

# Real processing path
def preprocess_signal(signal):
    filtered = []
    for x in signal:
        if x < 0:
            x = abs(x) ^ 3  # Bitwise distraction
        if x % 2 == 0:
            x = int(math.sqrt(x)) + 2
        else:
            x = (x + 1) // 2
        filtered.append(x * 3)
    return filtered

def transform_block(data):
    shifted = []
    for i, v in enumerate(data):
        if i % 3 == 0:
            shifted.append(v << 1)
        elif i % 3 == 1:
            shifted.append(v ^ (i * 2))
        else:
            shifted.append(v + (v & 7))
    return shifted

def accumulate_diagnostic(samples):
    stats = Counter()
    temp_diag = 0
    for s in samples:
        if s > 20:
            temp_diag += s >> 2
        elif s > 10:
            temp_diag += s % 7
        else:
            temp_diag -= s & 5
        stats['diagnostic'] += 1  # Red herring usage
    return temp_diag

def finalize_hash(buffer):
    seed = 101
    for b in buffer:
        seed = (seed * 31 + b) % 999983
    return seed

# Main execution with decoy variables and paths
if __name__ == "__main__":
    raw_input = [15, -4, 23, 0, 8, 19, -12, 6, 31, 5]
    
    # Irrelevant preprocessing branch
    outlier_threshold = 25
    anomalies = [x for x in raw_input if abs(x) > outlier_threshold]
    correction_factor = len(anomalies) * 0.5 if anomalies else 0.0
    
    # Actual relevant path starts here
    processed = preprocess_signal(raw_input)  # Step 1
    transformed = transform_block(processed)   # Step 2
    
    # Decoy analysis
    energy, peak, ent = analyze_readings(raw_input)
    diagnostic_score = accumulate_diagnostic(transformed)  # Another red herring
    
    # Critical path: build temp_buffer
    temp_buffer = []
    for i, val in enumerate(transformed):
        if i % 4 == 0:
            temp_buffer.append(val % 25)
        elif i % 4 == 2:
            temp_buffer.append((val + i) % 25)
    
    # Add constant padding (part of hash input)
    temp_buffer.extend([17, 23])
    
    # Key statement
    checksum = finalize_hash(temp_buffer)
    
    # Dead code branches
    if diagnostic_score < 0:
        checksum *= 2
    elif diagnostic_score == 0:
        checksum += 100
    
    # Final output
    Result: {checksum}