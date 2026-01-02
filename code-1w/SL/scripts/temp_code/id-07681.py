import itertools

def analyze_frequency(data):
    # Irrelevant function: analyzes character frequency but not used in main logic
    freq = {}
    for item in data:
        for c in str(item):
            freq[c] = freq.get(c, 0) + 1
    return freq

def validate_checksum(sequence):
    # Misleading validation that looks important but is never called
    return sum(sequence) % 10 == 0

def transform_chunk(chunk, mode=0):
    if mode == 0:
        return [x ** 2 - x for x in chunk]
    elif mode == 1:
        return [x + 10 for x in chunk if x % 2 == 0]
    else:
        return [x * 2 for x in chunk]

def filter_anomalies(log_data):
    # Dead code path - looks like it processes logs but isn't used
    threshold = 95
    return [entry for entry in log_data if entry < threshold]

def decode_signal(signal_stream):
    # Complex-looking transformation with red herring operations
    base_shift = 7
    adjusted = [(val + base_shift) * 2 for val in signal_stream]
    sliced = adjusted[::2]  # Every second element
    return [x - 5 for x in sliced]

def process_data(buffer):
    # Core logic hidden among distractions
    segment_a = buffer[:3]
    segment_b = buffer[3:6]
    
    # Distractor: unused transformed segments
    dummy_transform_1 = transform_chunk(segment_a, mode=0)
    dummy_transform_2 = transform_chunk(segment_b, mode=1)
    
    # Relevant computation begins here
    temp_result = []
    for i in range(len(segment_a)):
        if segment_a[i] % 2 == 0:
            temp_result.append(segment_a[i] * segment_b[i])
        else:
            temp_result.append(segment_a[i] + segment_b[i])
    
    # More misdirection: complex but unused list comprehension
    cross_product = [a * b for a, b in itertools.product(segment_a, segment_b) if a > 4 and b < 9]
    sorted_pairs = sorted([(segment_a[i], segment_b[i]) for i in range(3)], key=lambda x: x[0] - x[1])
    
    # Actual critical computation
    accumulator = 0
    for val in temp_result:
        if val > 10:
            accumulator += val // 2
        else:
            accumulator += val * 3
    
    # Final transformation using modular arithmetic and bit manipulation
    intermediate = (accumulator ^ 255) % 1000  # Bitwise XOR and mod
    final_value = intermediate * 2 - 17
    
    # Output the target result
    return final_value

# Simulated sensor data stream (meaningful input)
stream_buffer = [5, 8, 3, 6, 7, 4]

# Spurious variables to increase interference
checksum_valid = False
anomaly_count = 0
transform_log = []
reconstructed = None

# Unused recursive function - looks important but irrelevant
def build_tree(seq, depth=0):
    if depth >= 2 or len(seq) == 0:
        return None
    mid = len(seq) // 2
    return {
        'node': seq[mid],
        'left': build_tree(seq[:mid], depth+1),
        'right': build_tree(seq[mid+1:], depth+1)
    }

# Key execution point
final_output = process_data(stream_buffer)
print(f"Result: {final_output}")