from collections import defaultdict, Counter
import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing: applies noise filter that isn't used later
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]

def generate_checksum(sequence):
    # Distractor function: looks important but unused
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= int(val * 100) + i
    return chk % 1000

def evaluate_stability(ring_buffer):
    # Dead code path: never called
    moments = defaultdict(float)
    total = sum(ring_buffer)
    mean = total / len(ring_buffer)
    for x in ring_buffer:
        moments['variance'] += (x - mean) ** 2
    moments['variance'] /= len(ring_buffer)
    return moments['variance'] < 0.5

def transform_sequence(data, key_offset):
    # Applies XOR-based transformation with bit rotation
    shifted = []
    for i, val in enumerate(data):
        rotated = ((val << 1) | (val >> 7)) & 255  # 8-bit rotate left
        masked = rotated ^ key_offset
        shifted.append(masked)
    return shifted

def count_transitions(series):
    # Counts zero-crossings and significant jumps
    transitions = 0
    for i in range(1, len(series)):
        if (series[i-1] < 0 <= series[i]) or (series[i-1] >= 0 > series[i]):
            transitions += 1
        if abs(series[i] - series[i-1]) > 50:
            transitions += 1
    return transitions

def analyze_pattern(dataset, limit):
    stats = Counter()
    for item in dataset:
        if item % 2 == 0:
            stats['even'] += 1
        else:
            stats['odd'] += 1
        if item > limit:
            stats['high'] += 1
    balance_score = abs(stats['even'] - stats['odd'])
    return stats['high'] * 100 + (10 - min(balance_score, 10))

# Main execution flow
if __name__ == '__main__':
    # Input data: simulated sensor readings
    sensor_log = [12, 45, 67, 89, 13, 24, 35, 48, 56, 78, 81, 90, 102, 65, 54]

    # Irrelevant variables (red herrings)
    calibration_coefficients = [0.12, 0.34, 0.56, 0.78]
    baseline_shift = sum(calibration_coefficients) * 100
    temp_cache = defaultdict(int)
    for i in range(5):
        temp_cache[f'buffer_{i}'] = i * 10

    # Unused recursive function (decoy)
    def recursive_sum(n):
        return n + recursive_sum(n-1) if n > 0 else 0  # Never called

    # Step 1: Transform data using bitwise manipulation
    transformed_data = transform_sequence(sensor_log, key_offset=0b11010101)

    # Step 2: Compute auxiliary metrics (some irrelevant)
    transition_count = count_transitions(transformed_data)
    average_value = sum(transformed_data) / len(transformed_data)
    rounded_avg = round(average_value)

    # Step 3: Simulate diagnostic threshold based on environment
    env_factor = 4
    threshold = int(math.log(len(transformed_data)) * 20) + (env_factor ** 2)

    # Step 4: Core analysis (this produces the answer)
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Print result
    print(f"Result: {final_diagnostic}")