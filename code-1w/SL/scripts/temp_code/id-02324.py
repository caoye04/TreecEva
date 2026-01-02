import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal(base, noise_level):
    return [base + math.sin(i) * noise_level for i in range(5)]

def filter_outliers(data, limit):
    cleaned = []
    for x in data:
        if abs(x) < limit:
            cleaned.append(x * 0.9)
        else:
            cleaned.append(limit * 0.5)  # cap extreme values
    return cleaned

def compute_entropy(values):
    """Irrelevant helper: computes entropy but not used in final result"""
    total = sum(abs(v) for v in values)
    if total == 0:
        return 0.0
    probs = [abs(v) / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

def shift_phase(array, steps):
    """Misleading transformation: looks important but unused in critical path"""
    steps = steps % len(array)
    return array[steps:] + array[:steps]

def detect_anomaly_sequence(pattern):
    count = 0
    for i in range(1, len(pattern)):
        if pattern[i] > pattern[i-1] and pattern[i] % 2 == 1:
            count += 1
    return count > 2

def compress_data(seq):
    """Dead-end function: never actually contributes to final result"""
    return [seq[i] for i in range(0, len(seq), 2)]

def transform_readings(raw, factor):
    adjusted = []
    temp_offset = 0
    for val in raw:
        if val < 0:
            temp_offset += 1
        adjusted.append(abs(val) ** 0.5 * factor)
    adjustment_magnitude = temp_offset * factor  # Distractor variable
    return adjusted

def evaluate_stability(metrics):
    """Another red herring: computes stability index not used later"""
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    return variance < 5.0

def analyze_pattern(dataset, cutoff):
    # Core logic embedded within distractions
    aggregate = 0
    parity_flag = False
    
    for item in dataset:
        if item > cutoff:
            aggregate += int(item)
            if int(item) % 2 == 1:
                parity_flag = True
    
    # Critical conditional expression (required Python feature)
    modifier = 17 if parity_flag and aggregate > 30 else 23
    
    # Additional irrelevant computation
    dummy_sum = sum(math.cos(x) for x in dataset)
    normalized = aggregate * (1 + math.sin(dummy_sum))  # Looks complex, doesn't alter integer answer
    
    # Final result influenced only by core logic
    return int(normalized) + modifier

# Begin execution flow
initial_reading = acquire_signal(base=4, noise_level=2.5)

# Irrelevant intermediate processing chain
raw_spectrum = [math.exp(x/10) for x in initial_reading]
stability_score = evaluate_stability(raw_spectrum)  # Dead-end metric

# Main data path begins
filtered_stream = filter_outliers(initial_reading, limit=6.0)

# Apply phase shift that seems important but is discarded
shifted_buffer = shift_phase(filtered_stream, steps=2)
dummy_compressed = compress_data(shifted_buffer)  # Unused

# Transform readings - this affects final outcome
transformed_data = transform_readings(filtered_stream, factor=3.0)

# Another distraction: entropy calculation on wrong data
entropy_metric = compute_entropy(dummy_compressed)

threshold = 4.5

# Key statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

print(f"Result: {final_diagnostic}")