import itertools

# System health monitoring simulation with red herrings and complex data flow
def collect_telemetry(records):
    base_scores = [r['value'] * 0.7 + r['weight'] * 1.3 for r in records]
    adjusted = [abs(b - 50) ** 0.5 for b in base_scores]
    return adjusted

def generate_checksum(sequence):
    # Irrelevant function - looks important but unused in critical path
    return sum((i + v) * 2 for i, v in enumerate(sequence)) % 1000

def filter_outliers(data, threshold=15.0):
    # Mixes list comprehensions and conditional logic; some distraction
    upper = threshold * 1.8
    lower = threshold * 0.3
    filtered = [x for x in data if lower < x < upper]
    return filtered or [0]  # Avoid empty

def transform_readings(raw):
    # Uses lambda and conditional expressions
    modifier = lambda x: x * 1.1 if x < 20 else (x * 0.95 if x > 30 else x)
    return [modifier(val) for val in raw]

def compute_entropy(values):
    # Dead-end computation - not used in final result
    total = sum(values)
    probs = [(v / total) for v in values]
    from math import log
    return -sum(p * log(p) for p in probs if p > 0)

def multiplex_channels(data, channels=3):
    # Distracting combinatorics using itertools
    grouped = [data[i::channels] for i in range(channels)]
    transposed = list(itertools.zip_longest(*grouped, fillvalue=0))
    flattened = [item for group in transposed for item in group]
    return flattened[:len(data)]

def rolling_average(seq, window=3):
    # Unused auxiliary function - appears useful but irrelevant
    avgs = []
    for i in range(len(seq)):
        start = max(0, i - window + 1)
        avgs.append(sum(seq[start:i+1]) / (i - start + 1))
    return avgs

def extract_signatures(dataset):
    # Bit manipulation red herring
    sigs = []
    for d in dataset:
        bit_val = int(d) ^ 255  # XOR with constant
        bit_val = (bit_val << 2) | (bit_val >> 6)
        sigs.append(bit_val % 100)
    return sigs

def process_metrics(data, cfg):
    # Core logic buried among distractions
    stage1 = [x + cfg['offset'] for x in data]
    stage2 = [x * cfg['multiplier'] for x in stage1]
    
    # Conditional expression within transformation
    stage3 = [x if x > cfg['threshold'] else (x ** 2) + 5 for x in stage2]
    
    temp_shift = sum(stage3) / len(stage3)
    
    # Key branching logic
    if temp_shift > 40:
        result = int(temp_shift * 1.2)
    elif temp_shift > 25:
        result = int(temp_shift * 1.5)  # This will be taken
    else:
        result = int(temp_shift * 1.8)
        
    # Final adjustment based on parity (bitwise distraction)
    if result & 1:
        result ^= 7
    
    return result

# Simulated telemetry input
raw_records = [
    {'value': 28, 'weight': 12},
    {'value': 33, 'weight': 8},
    {'value': 19, 'weight': 15},
    {'value': 41, 'weight': 5},
    {'value': 25, 'weight': 10}
]

# Configuration map - some fields are decoys
config = {
    'offset': 3.5,
    'multiplier': 0.85,
    'threshold': 22.0,
    'timeout': 150,  # unused
    'retries': 3,     # unused
    'mode': 'safe'    # unused
}

# Execution chain with multiple diversions
telemetry_scores = collect_telemetry(raw_records)
filtered_scores = filter_outliers(telemetry_scores, threshold=14.5)
transformed_data = transform_readings(filtered_scores)

# Multiple irrelevant operations to obscure the main flow
checksum = generate_checksum(transformed_data)  # dead end
entropy = compute_entropy(transformed_data)   # irrelevant
signatures = extract_signatures(transformed_data)  # red herring
rolled = rolling_average(transformed_data, window=2)  # unused
multiplexed = multiplex_channels(transformed_data, channels=3)  # distractor

# Critical execution point
final_diagnostic = process_metrics(transformed_data, config)

# Output the required result
print(f"Result: {final_diagnostic}")