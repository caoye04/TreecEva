import math

# Simulated sensor data preprocessing with diagnostic flags
def preprocess_sensor_readings(raw_readings):
    processed = {}
    for key, values in raw_readings.items():
        filtered = [x for x in values if x > -100 and x < 100]
        smoothed = sum(filtered) / len(filtered) if filtered else 0
        processed[key] = round(smoothed, 3)
    return processed

# Irrelevant helper - dead path (never called)
def legacy_normalization(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Data transformation pipeline with decoy logic
def apply_frequency_shift(signal, shift_factor):
    shifted = []
    for i, val in enumerate(signal):
        shifted.append(val * math.sin(i * shift_factor))
    return shifted

# Misleading entropy calculation (unused later)
def calculate_entropy(arr):
    from collections import Counter
    counts = Counter(arr)
    total = len(arr)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

# Core processing function with critical logic
def encode_features(data_dict):
    encoded = []
    for k, v in data_dict.items():
        encoded.append(hash(k) % 100 + v * 2)
    return encoded

# Decoy state tracker (looks important but unused)
class StateRegistry:
    def __init__(self):
        self.records = []
    def log(self, entry):
        self.records.append(entry)

registry = StateRegistry()
registry.log('INIT')

# Higher-order function with lambda abstraction
def create_filter(threshold):
    return lambda x: x > threshold

# Dictionary-based routing map (some entries are red herrings)
routing_map = {
    'A1': {'path': 'primary', 'weight': 0.8},
    'B2': {'path': 'secondary', 'weight': 0.5},
    'C3': {'path': 'debug', 'weight': 0.1},  # unused debug path
    'D4': {'path': 'legacy', 'weight': 0.0}   # deprecated
}

# Data transformation using case conversion as distraction
def transform_keys(data):
    new_data = {}
    for k, v in data.items():
        upper_k = k.upper()
        if upper_k.startswith('A') or upper_k.startswith('B'):
            new_data[upper_k] = v * 1.1
        elif upper_k.startswith('C'):
            new_data[upper_k.lower()] = v * 0.9  # alternate path never triggered
        else:
            new_data[k] = v
    return new_data

# Main metric processor with critical computation
def process_metrics(data, cfg):
    base_score = 0
    adjustment = cfg.get('adjustment', 0)
    
    for key, value in data.items():
        if key in ['TEMP_01', 'PRESS_02']:
            base_score += value * 3
        elif key == 'FLOW_03':
            base_score += value * 2.5
    
    # Critical manipulation using sorting side effect
    sorted_values = sorted(data.values(), reverse=True)
    penalty = sorted_values[2] * 0.2  # third highest value penalty
    
    result = base_score - penalty + adjustment
    
    # Bit manipulation red herring
    bit_analysis = (int(result) >> 3) & 0xFF
    registry.log(f'BIT_ANALYSIS: {bit_analysis}')
    
    return round(result, 4)

# Setup: Real data flow with distractions
raw_sensor_data = {
    'temp_01': [23.5, 24.1, 22.8, 150, -200],  # includes outliers
    'press_02': [101.3, 102.1, 100.9],
    'flow_03': [45.6, 46.2, 44.9, 47.0],
    'vib_04': [0.3, 0.5, 0.4]  # irrelevant metric
}

# Apply real preprocessing
clean_data = preprocess_sensor_readings(raw_sensor_data)

# Transform keys to uppercase (impacting routing lookup)
transformed_data = transform_keys(clean_data)

# Unused sorting distraction
name_list = ['Alice', 'Bob', 'Charlie', 'Diana']
sorted_names = sorted(name_list, key=lambda name: len(name))

# Configuration with misleading fields
class Config:
    def __init__(self):
        self.adjustment = 7.5
        self.threshold = 40.0
        self.debug_mode = True
        self.timeout = 5000

config = Config().__dict__

# Critical filtering operation (uses lambda)
high_flow_filter = create_filter(config['threshold'])
flow_value = transformed_data.get('FLOW_03', 0)

# Dead branch - never executed
if high_flow_filter(flow_value):
    adjusted_flow = flow_value * 1.2
else:
    adjusted_flow = flow_value * 0.8  # this runs but doesn't affect final answer

# Final diagnostic calculation - KEY STATEMENT
final_diagnostic = process_metrics(transformed_data, config)

# Output the target result
print(f"Result: {final_diagnostic}")