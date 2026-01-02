from collections import defaultdict, Counter
import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing: applies noise filter that isn't used later
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    stats = defaultdict(int)
    for val in filtered:
        stats['count'] += 1
        stats['sum'] += val
    return [int(x * 10) for x in raw_samples]  # Only this line matters

def generate_key_stream(length):
    # Distractor function: generates unused cryptographic-looking sequence
    stream = [1]
    for i in range(1, length):
        stream.append((stream[-1] * 7 + 3) % 16)
    return stream[::-1]  # Never actually used

def transform_readings(readings):
    # Main transformation with red herring operations
    temp_log = []
    checksum = 0
    for i, val in enumerate(readings):
        if i % 3 == 0:
            temp_log.append(val ** 2)
        elif i % 3 == 1:
            temp_log.append(abs(val - 5))
        else:
            temp_log.append(val // 2)
        checksum += val
    
    # Dead code path (never reached due to return)
    if checksum < 0:
        return [x * -1 for x in temp_log]
    
    # This is the actual used transformation
    return [x % 9 for x in temp_log]

def recursive_reduce(sequence, depth=0):
    # Simple recursion with modular arithmetic
    if depth >= 3 or len(sequence) == 1:
        return sequence[0] if sequence else 0
    reduced = []
    for i in range(0, len(sequence), 2):
        if i + 1 < len(sequence):
            reduced.append((sequence[i] + sequence[i+1]) % 11)
        else:
            reduced.append(sequence[i])
    return recursive_reduce(reduced, depth + 1)

def analyze_pattern(data, reference):
    # Core logic with multiple distractions
    
    # Irrelevant analysis block
    freq_map = Counter(data)
    mode_val = max(freq_map, key=freq_map.get)
    entropy = 0
    total = len(data)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    
    # Decoy computation using string methods (seemingly important but unused)
    signature = ''.join([str(x % 10) for x in data[:5]])
    mask = signature.translate(str.maketrans('012345', '543210'))
    probe = int(mask[:3]) if len(mask) >= 3 else 0
    
    # Real computation begins here
    weighted_sum = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            weighted_sum += val * (reference[i % len(reference)] % 7)
        else:
            weighted_sum -= (val * 2) % 5
    
    # Critical branching based on subtle condition
    adjustment_factor = 1
    if len(data) > 10 and data[0] == 4:
        adjustment_factor = 2
    
    intermediate = abs(weighted_sum) * adjustment_factor
    
    # Final reduction using recursion
    history = [intermediate % 100]
    for i in range(4):
        history.append((history[-1] * 2 + i) % 89)
    
    final_value = recursive_reduce(history)  # Actual answer source
    
    # Dead assignment
    final_value = final_value * 1 if final_value != 0 else 1
    
    return final_value

# Simulated sensor input (deterministic)
raw_sensor_data = [3.1, 4.2, 5.3, 6.4, 2.5, 3.6, 4.7, 5.8, 6.9, 1.0, 2.1]

# Unused variables - red herrings
baseline_calibration = generate_key_stream(10)
system_status = {'phase': 'idle', 'mode': 'diagnostic', 'checksum_valid': False}
error_buffer = [0] * 15

# Key sequence for pattern analysis
key_sequence = [3, 7, 2, 8, 1, 4, 6]

# Main data flow
processed_samples = preprocess_signal(raw_sensor_data)
transformed_data = transform_readings(processed_samples)

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, key_sequence)

print(f"Result: {final_diagnostic}")