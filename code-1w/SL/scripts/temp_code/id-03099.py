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

def generate_sequence(n):
    # Distractor function: generates Fibonacci-like sequence never used
    seq = [1, 1]
    for i in range(2, n + 5):
        seq.append(seq[i-1] + seq[i-2])
    return seq

def evaluate_health_index(measurements):
    # Dead code path: computes health score but never returned or used
    average = sum(measurements) / len(measurements)
    variance = sum((x - average) ** 2 for x in measurements) / len(measurements)
    return math.exp(-variance)

def shift_window(data, window_size=3):
    # Real transformation: creates overlapping XOR windows
    result = []
    for i in range(len(data) - window_size + 1):
        window_xor = 0
        for j in range(window_size):
            window_xor ^= data[i + j]
        result.append(window_xor)
    return result

def decode_signature(signal):
    # Misleading intermediate: performs bit rotation that seems important
    rotated = [(x << 1) | (x >> 7) for x in signal]
    count_freq = Counter(rotated)
    most_common_shift = count_freq.most_common(1)[0][1]
    return [x for x in rotated if x % 2 == 0]  # Unused return

def analyze_pattern(data, threshold):
    # Critical logic: counts how many elements exceed threshold after sorting
    sorted_data = sorted(data, reverse=True)
    above_threshold = [x for x in sorted_data if x > threshold]
    cumulative = 0
    for val in above_threshold:
        if val % 2 == 0:
            cumulative += val // 2
        else:
            cumulative -= -(val // -2)  # Ceiling division simulation
    return cumulative + len(above_threshold)

# Main execution with red herrings
raw_sensor_data = [0.15, -0.3, 0.45, 0.6, -0.75, 0.9, 1.05, -1.2, 1.35, 1.5]
processed_noise = evaluate_health_index(raw_sensor_data)  # Dead call

# Key data transformation chain
transformed_data = preprocess_signal(raw_sensor_data)
decoded_part = decode_signature(transformed_data)  # Computed but unused
windowed_data = shift_window(transformed_data, 3)

# Generate irrelevant sequence that looks diagnostic
phantom_diagnosis = generate_sequence(8)

key_threshold = 5
final_diagnostic = analyze_pattern(windowed_data, key_threshold)

# Print required output
print(f"Result: {final_diagnostic}")