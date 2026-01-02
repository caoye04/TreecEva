import math

# Irrelevant helper function (dead code path)
def unused_signal_processor(x):
    return [i * 1.5 for i in x if i > 3]

# Misleading data transformation
temp_snapshot = [18, 22, 19, 25, 40, 17]
scaled_buffer = [round(math.log(x) * 2, 2) for x in temp_snapshot if x > 15]

# Core system: Biomedical metric analyzer
def evaluate_stability(readings, config):
    baseline = config.get('baseline', 20)
    tolerance = config.get('tolerance', 5)
    
    # Compute moving average over valid windows
    filtered = [x for x in readings if 10 < x < 50]
    avg = sum(filtered) / len(filtered) if filtered else 0
    
    # Apply nonlinear response curve
    deviation = abs(avg - baseline)
    stress_index = int((deviation / tolerance) ** 1.5)
    
    return {'avg': avg, 'index': stress_index, 'stable': stress_index < 3}

# Unused diagnostic mode (distractor)
class LegacyAnalyzer:
    def __init__(self, data):
        self.data = data
        self.result = None
    
    def run_legacy(self):
        return sum(self.data) % 7

# Real processing begins here
raw_data = [23, 18, 25, 21, 19, 24, 20, 22]

# Complex configuration with red herring fields
thresholds = {
    'baseline': 21,
    'tolerance': 4,
    'activation': 0.75,
    'ignore_outliers': False,
    'calibration_offset': 1.02,
    'deprecated_mode': True
}

# Auxiliary computation (irrelevant to final result)
outlier_flags = {i: val > 23 for i, val in enumerate(raw_data)}
flag_sum = sum(1 for f in outlier_flags.values() if f)

# Secondary data structure (decoy usage)
metadata_log = [
    {'timestamp': 'T1', 'value': 23, 'type': 'A'},
    {'timestamp': 'T2', 'value': 18, 'type': 'B'}
]

# Bit manipulation distraction
bitmask = 0
for entry in metadata_log:
    bitmask ^= len(entry['timestamp']) << 2

# Primary analysis pipeline
health_data = [x + 0.5 for x in raw_data if x % 2 == 0]  # Only even values adjusted

# Conditional override that never triggers (misleading)
if len(health_data) > 10 and False:  # Dead logic branch
    health_data = [30.0] * 3

# Core evaluation using dictionary and list comprehension
analysis = evaluate_stability(health_data, thresholds)

# Additional irrelevant aggregation
duplicate_check = set([x for x in raw_data for _ in range(2)])
size_metric = len(duplicate_check) * 2

# Final multi-step diagnostic logic
if analysis['stable']:
    confidence = 90 + (2 if analysis['index'] == 0 else 5)
else:
    confidence = 50 - analysis['index'] * 8

# Critical answer computation
base_score = int(analysis['avg'] * 10)
adjustment = 7 if confidence > 80 else -3
final_diagnostic = base_score + adjustment + (1 if flag_sum % 2 else 0)

# Output the required result
print(f"Result: {final_diagnostic}")