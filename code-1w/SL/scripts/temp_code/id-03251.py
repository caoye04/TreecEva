import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_B = -0.013
TEMPORAL_DAMPING = 0.05
MAX_BUFFER_SIZE = 1024

# Misleading auxiliary data structures
decoys = {
    'phantom_metric_1': [0.1, 0.2, 0.3],
    'ghost_index': set([999, 888, 777]),
    'bogus_flags': {'erroneous': True, 'invalid': False}
}

# Real input data
raw_readings = [12, 15, 22, 8, 31, 44, 19, 7]

def preprocess(sensor_data):
    """Apply irrelevant smoothing and extract meaningful features"""
    smoothed = []
    for i in range(len(sensor_data)):
        # Distractor computation (not used later)
        if i > 0:
            prev_val = sensor_data[i-1] * TEMPORAL_DAMPING
        smoothed.append(int(math.sqrt(sensor_data[i]) * 10))
    
    # Actual relevant transformation
    return [x * 2 for x in sensor_data if x > 10]  # Only values >10, doubled

# Decoy function that looks important but is never called
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Another red herring: complex structure with unused logic
class DiagnosticFilter:
    def __init__(self, level):
        self.level = level
        self.buffer = []
        self.active = False  # Never activated

    def update(self, val):
        if self.active:  # Always false
            self.buffer.append(val)

filter_chain = [DiagnosticFilter(1), DiagnosticFilter(2)]

# Threshold configuration (critical for final logic)
threshold_map = {
    'low_risk': 20,
    'warning': 35,
    'critical': 50
}

# Secondary distractor: unused statistical summary
data_stats = {
    'mean_proxy': sum(raw_readings) / len(raw_readings),
    'peak': max(raw_readings),
    'baseline_offset': CALIBRATION_FACTOR_A * 5
}

# Process the data through the real pipeline
processed_data = preprocess(raw_readings)

# Simulate conditional early exit (not triggered)
if len(processed_data) == 0:
    final_diagnostic = -1
    print(f"Result: {final_diagnostic}")
else:
    # Real analysis begins here
    risk_levels = []
    
    for val in processed_data:
        category = None
        if val < threshold_map['low_risk']:
            category = 1
        elif val < threshold_map['warning']:
            category = 2
        elif val < threshold_map['critical']:
            category = 3
        else:
            category = 4
        risk_levels.append(category)
    
    # Accumulate weighted score
    score = 0
    weights = {1: 1, 2: 3, 3: 6, 4: 10}
    for level in risk_levels:
        score += weights[level]
    
    # Introduce decoy calculation with sets and tuples (unused)
    unique_risks = set(risk_levels)
    risk_pairs = [(a, b) for a in unique_risks for b in unique_risks if a < b]
    tuple_sum = sum([t[0] + t[1] for t in risk_pairs])  # Dead computation
    
    # Additional distraction: dictionary comprehension with no effect
    normalized = {k: v / sum(weights.values()) for k, v in weights.items()}
    
    # Final diagnostic logic (depends only on score)
    if score > 20:
        final_diagnostic = score * 2 + 10
    elif score > 10:
        final_diagnostic = score * 3
    else:
        final_diagnostic = score * 5 - 5

# Print result as required
print(f"Result: {final_diagnostic}")