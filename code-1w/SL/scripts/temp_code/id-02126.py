import math

# Simulated sensor data and calibration constants (irrelevant values included)
sensor_offsets = [0.1, -0.3, 0.5, 0.0, 0.2]
dummy_calibrations = {(i, j): (i * 1.5 + j * 0.7) for i in range(4) for j in range(4)}
baseline_noise_floor = 0.041

# Real processing begins here — but obscured by distractions
def generate_frequency_map(raw_values):
    # Irrelevant frequency mapping (unused later)
    return {i: math.sin(v * math.pi / 4) for i, v in enumerate(raw_values)}

# Unused helper — red herring
class SignalNormalizer:
    def __init__(self, factor=1.0):
        self.factor = factor

    def normalize(self, x):
        return x * self.factor

# Key transformation pipeline
def transform_sequence(seq):
    # Apply bitwise masking to simulate digital filtering
    masked = [v & 7 for v in seq]  # Keep only last 3 bits
    shifted = [(v << 1) ^ 3 for v in masked]  # Left shift and XOR with 3
    return [s % 10 for s in shifted]  # Wrap to single digit

def encode_features(data_list):
    # Use list comprehension with conditional logic
    encoded = [
        (x * 2) + 1 if i % 2 == 0 else (x + 5) 
        for i, x in enumerate(data_list)
    ]
    # Decoy operation — result unused
    reversed_pairs = [(encoded[i], encoded[-i-1]) for i in range(len(encoded)//2)]
    return encoded

def aggregate_metrics(temporal):
    # Compute running checksum with lambda-based weighting
    weight_fn = lambda idx: 0.9 ** idx
    weighted_sum = sum(temporal[i] * weight_fn(i) for i in range(len(temporal)))
    avg = weighted_sum / len(temporal) if temporal else 0
    return round(avg * 1000)  # Scale up for precision

def detect_anomalies(arr):
    # Dummy detection using set operations (irrelevant)
    threshold_set = {2, 4, 6}
    detected = {x for x in arr if x in threshold_set}
    return len(detected) > 0

def analyze_signal(cleaned):
    # Core logic hidden among noise
    base_value = sum(cleaned) * 3
    adjustment = cleaned[0] - cleaned[-1]
    temp_result = base_value + (adjustment * 10)
    
    # Additional real computation
    if temp_result > 100:
        temp_result = temp_result // 2
    
    # Final diagnostic calculation
    final_diagnostic = abs(temp_result - 42) * 2
    return final_diagnostic

# Orchestration with decoy calls
raw_input_data = [12, 8, 15, 3, 7]

# Distraction: Unused signal normalization
normalizer = SignalNormalizer(factor=0.95)
normalized = [normalizer.normalize(x) for x in raw_input_data]

# Generate irrelevant frequency map
_ = generate_frequency_map(raw_input_data)

# Real processing chain
filtered = transform_sequence(raw_input_data)
processed_data = encode_features(filtered)
interim_score = aggregate_metrics(processed_data)  # Misleading name
has_issue = detect_anomalies(processed_data)  # Dead-end check

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")