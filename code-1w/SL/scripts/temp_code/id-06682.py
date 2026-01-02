import math

# Simulated sensor data and diagnostic system with distractors
def collect_samples():
    return [0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10.0]

def filter_noise(data, threshold=0.5):
    # Irrelevant filtering (not used in final path)
    return [x for x in data if x > threshold]

def compute_envelope(signal):
    # Real processing: computes square root of each element
    return [math.sqrt(x) for x in signal]

def count_transitions(data):
    # Distractor function: counts sign changes (always positive here)
    transitions = 0
    for i in range(1, len(data)):
        if data[i] * data[i-1] < 0:
            transitions += 1
    return transitions

def generate_checksum(sequence):
    # Dead code path — looks important but unused
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 10)  # bit manipulation red herring
    return checksum

def validate_coherence(data):
    # Misleading validation that returns constant
    if len(data) % 2 == 0:
        return sum([d ** 0.5 for d in data[::2]])  # partial slice distraction
    else:
        return -1

def accumulate_magnitude(signal):
    # Relevant accumulation: sum of integer parts
    magnitude = 0
    for val in signal:
        magnitude += int(val)
    return magnitude

def extract_features(dataset):
    # Nested logic with slicing and conditional expressions
    size = len(dataset)
    midpoint = size // 2
    left_half = dataset[:midpoint]
    right_half = dataset[midpoint:]
    
    # Conditional expression used
    dominant = left_half if sum(left_half) >= sum(right_half) else right_half
    
    # Feature: variance-like calculation on dominant half
    mean_val = sum(dominant) / len(dominant)
    variance_proxy = sum((x - mean_val) ** 2 for x in dominant) / len(dominant)
    
    # Return multiple values; only one is used later
    return {
        'avg': mean_val,
        'variance': variance_proxy,
        'peak': max(dominant),
        'count_above_mean': len([x for x in dominant if x > mean_val])
    }

def analyze_signal(data_package):
    # Main analysis with set operations and distractions
    raw_values = {round(v, 1) for v in data_package}  # set operation
    scaled_values = {v * 2 for v in raw_values if v > 1.0}  # filtered set comprehension
    
    # Key computation hidden among distractors
    base_score = 0
    for val in data_package:
        if val.is_integer():
            base_score += int(val) ** 2
        else:
            base_score -= int(val)
    
    # Accumulate magnitude from another function
    extra_boost = accumulate_magnitude(data_package)
    
    # Final result depends only on base_score and extra_boost
    final_score = base_score + extra_boost
    
    # Decoy return fields
    diagnostics = {
        'status': 'OK',
        'readings': len(data_package),
        'checksum': generate_checksum(data_package),
        'transitions': count_transitions(data_package),
        'coherence': validate_coherence(data_package),
        'final_diagnostic': final_score  # This is the key variable
    }
    
    return diagnostics['final_diagnostic']

# --- Execution ---
data_stream = collect_samples()
filtered_data = filter_noise(data_stream)  # irrelevant assignment
processed_data = compute_envelope(data_stream)  # actual input to analysis
features = extract_features(processed_data)  # distractor call

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")