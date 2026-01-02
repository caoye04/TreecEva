import itertools

# Simulated sensor data processing with red herrings and complex transformations
def collect_signals():
    raw_readings = [12, 45, 23, 67, 89, 34, 56, 78, 90, 11]
    offset = 5
    adjusted = [x - offset for x in raw_readings]
    return adjusted

def apply_filter(data, mode='low'):
    if mode == 'low':
        return [x for x in data if x < 50]
    else:
        return [x for x in data if x >= 50]

# Irrelevant helper - dead path
def decrypt_sequence(seq):
    return [((x * 3) + 7) % 256 for x in seq][::-1]

# Unused transformation chain
def legacy_process(stream):
    stream.reverse()
    return [x >> 2 for x in stream]

def generate_pairs(values):
    # Creates distraction tuples
    pairs = list(itertools.combinations(values, 2))
    sums = [a + b for a, b in pairs]
    products = [a * b for a, b in pairs]
    return sums, products  # Never used

def transform_readings(readings):
    # Actual relevant slicing and transformation
    segment_a = readings[1:6:2]  # indices 1,3,5 -> values: 40, 62, 84
    segment_b = readings[-3::-3]  # indices -3, -6, -9 -> values: 51, 45, 10
    combined = segment_a + segment_b
    
    # Distractor: meaningless bitwise ops
    magic_mask = 0b1101
    masked_vals = [(x ^ magic_mask) & 0xFF for x in combined]
    
    # More noise: case conversion simulation (irrelevant)
    labels = ['A', 'B', 'C', 'D']
    label_map = {k: v.lower() for k, v in zip(labels, labels)}
    
    # Critical transformation
    processed = [x // 2 for x in combined if x % 2 == 0]  # Only even numbers, halved
    return processed

def analyze_pattern(data):
    # Real logic: sum of squares of first three elements
    truncated = data[:3]
    squares = [x ** 2 for x in truncated]
    total = sum(squares)
    
    # Decoy recursion (never reached)
    def recursive_decay(n, depth=0):
        if depth >= 3 or n < 10:
            return n
        return recursive_decay(n - (n // 4), depth + 1)
    
    # Fake control flow
    flag = False
    if len(data) > 100:
        final_value = recursive_decay(total)
    else:
        final_value = total  # This actually executes
    
    # Spurious set operation
    unique_check = set(data)
    if len(unique_check) == len(data):
        pass  # Do nothing
    
    return final_value

# Main execution chain
sensor_log = collect_signals()
filtered_data = apply_filter(sensor_log, mode='low')
decoded_stream = decrypt_sequence(sensor_log)  # Computed but unused
legacy_result = legacy_process(sensor_log[:])  # Dead call
sum_list, prod_list = generate_pairs(filtered_data)  # Unused tuple unpacking
transformed_data = transform_readings(sensor_log)
final_diagnostic = analyze_pattern(transformed_data)
print(f"Target result: {final_diagnostic}")