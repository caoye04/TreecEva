import itertools

# Simulated sensor data with noise and metadata
raw_readings = [15, -8, 22, 44, -3, 9, 11, 4, 33, -1, 2]
metadata_tags = ['A', 'B', 'C', 'D', 'E']

def generate_checksum(sequence):
    # Irrelevant function: computes a checksum but not used in main logic
    return sum(x ** 2 for x in sequence if x > 0) % 100

def filter_outliers(stream, threshold=10):
    # Filters values exceeding threshold (absolute)
    return [x for x in stream if abs(x) <= threshold]

def accumulate_with_decay(values, decay_factor=0.9):
    # Applies exponential decay to cumulative sum
    total = 0.0
    for i, val in enumerate(values):
        total += val * (decay_factor ** i)
    return total

def extract_patterns(seq):
    # Uses itertools to find repeating pairs — red herring
    pairs = list(itertools.pairwise(seq))
    repeats = [p for p in pairs if p[0] == p[1]]
    return len(repeats)

def validate_sequence(seq):
    # Dummy validation that always passes — misleading
    if len(seq) < 5:
        return False
    running = 0
    for x in seq:
        running = (running * 3 + x) % 17
    return running == 12  # Never actually checked

def transform_data(packet):
    # Applies bit manipulation for no effect — distractor
    transformed = []
    for x in packet:
        manipulated = (x << 2) ^ 0b1010
        if manipulated > 100:
            manipulated -= 50
        transformed.append(abs(manipulated) % 50)
    return transformed

def compute_entropy(values):
    # Unused advanced calculation — dead path
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

def analyze_trend(numbers):
    # Another unused analysis function
    increasing = sum(1 for a, b in itertools.pairwise(numbers) if b > a)
    decreasing = sum(1 for a, b in itertools.pairwise(numbers) if b < a)
    return 'up' if increasing > decreasing else 'down'

def process_results(input_data):
    # Core logic hidden among distractions
    stage1 = filter_outliers(input_data)  # [-8, 9, 4, -1, 2]
    
    # Misleading intermediate transformations
    dummy_seq = [x + 10 for x in stage1 if x % 2 == 0]  # [2, 14] -> distractor
    temp_flag = any(x > 12 for x in dummy_seq)  # False, irrelevant
    
    # Real processing begins here
    cleaned = [x for x in stage1 if x >= 0]  # [9, 4, 2]
    base_sum = sum(cleaned)  # 15
    
    # Apply decay accumulation
    score_component = accumulate_with_decay(cleaned, 0.8)  # 9*1 + 4*0.8 + 2*0.64 = 9 + 3.2 + 1.28 = 13.48
    
    # Add bonus if certain condition met (hidden logic)
    bonus = 10 if len(cleaned) == 3 and base_sum > 10 else 0  # Triggered: 10
    final = int(score_component + bonus)  # 13.48 + 10 = 23.48 → 23
    
    # Dead branch — looks important but unused
    if final > 20:
        audit_log = transform_data([final])
        checksum = generate_checksum(audit_log)
    
    return final

# Simulate data ingestion pipeline
buffer_cache = raw_readings.copy()

# Preprocess phase (includes useless operations)
data_profile = {
    'length': len(raw_readings),
    'positive_count': len([x for x in raw_readings if x > 0]),
    'checksum_hint': generate_checksum(raw_readings[:5]),  # 15²+(-8)²+22²+44²+(-3)² = 225+64+484+1936+9 = 2718 % 100 = 18
    'trend': analyze_trend(raw_readings)
}

# Apply transformation that isn't used later
shadow_copy = transform_data(buffer_cache)

# Main execution point
final_score = process_results(raw_readings)

# Output result as required
print(f"Result: {final_score}")