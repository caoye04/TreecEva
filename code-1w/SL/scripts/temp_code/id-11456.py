import math

# Simulated sensor data and calibration constants (mostly irrelevant)
def calibrate_sensor(raw_input, offset=0.13):
    return [x + offset for x in raw_input if x > 0.5]

def preprocess_signal(data_stream):
    # Real preprocessing step: normalize and filter noise
    normalized = [val / max(data_stream) for val in data_stream]
    filtered = [v for v in normalized if v > 0.1]
    return filtered

# Misleading transformation chain
def transform_v1(x):
    return x ** 2 + 2 * x + 1

def transform_v2(x):
    return x * 1.5 - 0.2

def transform_v3(x):
    return math.log(x + 1) if x >= 0 else 0

# Unused recursive red herring
def useless_recursion(n):
    if n <= 1:
        return 1
    return n * useless_recursion(n - 2)

# Distractor: complex but unused data structure
class DiagnosticBuffer:
    def __init__(self):
        self.buffer = {}
        self.counter = 0
    
    def add_entry(self, key, value):
        self.buffer[key] = value
        self.counter += 1

    def get_summary(self):
        return sum(self.buffer.values())

# Another decoy function with plausible but unused logic
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Core relevant logic hidden among noise
def extract_features(signal):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    peak_ratio = max(signal) / mean_val
    return mean_val, variance, peak_ratio

# Main analysis with critical computation
def analyze_signal(cleaned_signal):
    feature_set = extract_features(cleaned_signal)
    
    # Irrelevant weighting scheme
    weights = {'w1': 0.7, 'w2': 0.2, 'w3': 0.1}
    dummy_score = sum(feature_set[i] * list(weights.values())[i % 3] for i in range(len(feature_set)))
    
    # Actual answer path: uses feature_set[1] (variance) in a deterministic way
    temp_state = int(feature_set[1] * 1000)  # Convert variance to integer seed
    accumulator = 0
    for i in range(1, temp_state % 97 + 1):  # bounded loop
        if i % 3 == 0:
            accumulator += i * 2
        elif i % 5 == 0:
            accumulator -= i
    
    # Final computation — this is what matters
    final_diagnostic = accumulator + int(feature_set[0] * 100)  # depends on mean_val
    return final_diagnostic

# Generate initial data (deterministic)
raw_sensor_data = [23, 45, 67, 89, 12, 34, 56, 78]

# Chain of operations with many distractions
adjusted_data = calibrate_sensor([x / 100 for x in raw_sensor_data], offset=0.13)
processed_data = preprocess_signal(adjusted_data)

# Dead code path — never called
buffer = DiagnosticBuffer()
for idx, val in enumerate(processed_data):
    buffer.add_entry(f'entry_{idx}', transform_v1(val))

# Key statement: this triggers the answer computation
final_diagnostic = analyze_signal(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")