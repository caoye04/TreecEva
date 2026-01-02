from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings
def preprocess_signal(raw):    
    # Irrelevant transformation (distractor)
    smoothed = [x * 0.9 + 5 for x in raw]
    filtered = [x for x in smoothed if x > 10]
    return filtered

# Unused function - dead code path (distractor)
def legacy_calibrate(data):
    return [x / 1.1 for x in data]

# Core logic buried in noise
def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])  # Fibonacci-like sequence
    return seq

def transform_readings(readings, mode='fast'):
    # Real computation mixed with distractions
    temp_log = []
    scaling_factor = 3.7
    offset = 2
    
    # Distractor: unused counters
    diagnostic_count = defaultdict(int)
    event_tracker = Counter()
    
    for val in readings:
        if val % 2 == 0:
            transformed = (val ** 1.5) / scaling_factor
        else:
            transformed = abs(math.sin(val)) * scaling_factor + offset
        temp_log.append(round(transformed, 3))
    
    # Actual relevant transformation
    sliced = temp_log[::2]  # Slicing operation (required feature)
    return [x * 1.1 for x in sliced]

# Recursive pattern analyzer (core concept)
def analyze_pattern(data, limit):
    if len(data) <= 1:
        return int(sum(data))
    
    mid = len(data) // 2
    left = analyze_pattern(data[:mid], limit)
    right = analyze_pattern(data[mid:], limit)
    
    # Key computation
    return (left * 2) - right + (1 if left > limit else -1)

# Misleading high-complexity function that isn't used
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Decoy data structures
audit_trail = []
diagnostic_cache = set()
system_flags = {'active': True, 'debug': False, 'legacy_mode': False}

# Real data generation buried in setup
base_sequence = generate_sequence(12)
raw_sensor_data = [x * 2 for x in base_sequence if x % 3 != 0]

# Apply real preprocessing
processed_batch = preprocess_signal(raw_sensor_data)

# Transform using slicing and mathematical operations
transformed_data = transform_readings(processed_batch, mode='fast')

# Threshold derived from recursive sequence property
threshold = base_sequence[5]  # 8

# Critical statement containing the answer
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")