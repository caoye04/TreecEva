import math

# Simulate sensor data processing with noise filtering and pattern detection
def collect_sensor_readings():
    raw_readings = [12.5, 13.0, 11.8, 9.7, 14.2, 15.0, 10.3, 13.8]
    filtered = list(filter(lambda x: x > 10.0, raw_readings))
    normalized = [(x - 10.0) / 5.0 for x in filtered]
    return normalized


def generate_checksum(sequence):
    # Irrelevant helper: computes a checksum but not used in final logic
    return sum(i * val for i, val in enumerate(sequence)) % 100


def augment_data(seq):
    # Adds synthetic data points using trigonometric modulation (some distraction)
    extended = []
    for i, val in enumerate(seq):
        modulated = val * math.sin(i + 1)
        extended.append(abs(modulated))
    return extended + [0.1, 0.2]  # Additional irrelevant padding


def count_peaks(data):
    # Counts local maxima above threshold
    peaks = 0
    for i in range(1, len(data) - 1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > 0.5:
            peaks += 1
    return peaks


def compute_entropy(values):
    # Calculates Shannon entropy (semi-relevant but not directly used)
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def extract_features(signal):
    # Extracts statistical features; some are later ignored
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    peak_count = count_peaks(signal)
    
    # Red herring computation
    dummy_score = (mean_val * 2 + math.sqrt(variance)) % 7
    
    # Only peak_count and length are actually used later
    return {
        'length': len(signal),
        'peaks': peak_count,
        'avg': mean_val,
        'var': variance,
        'score': dummy_score  # unused downstream
    }


def analyze_signal(dataset):
    # Main analysis function
    stats = extract_features(dataset)
    
    # Distractor: complex-looking but unused transformation
    transformed = [math.tanh(x) for x in dataset]
    temp_sum = sum(transformed)
    temp_norm = temp_sum / len(transformed) if transformed else 0
    
    # Real logic: uses only two fields from stats
    base = stats['length']
    modifier = stats['peaks']
    
    # Core calculation
    intermediate = (base * 7) + (modifier * 3)
    
    # Apply modular adjustment based on sum of digits in base value
    digit_sum = sum(int(d) for d in str(base))
    adjusted = intermediate - digit_sum
n    
    # Final diagnostic derived from adjusted value
    final_diagnostic = adjusted * 2
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_readings()
augmented_data = augment_data(sensor_data)
processed_data = augment_data(augmented_data)  # Double augmentation - one is redundant
final_diagnostic = analyze_signal(processed_data)