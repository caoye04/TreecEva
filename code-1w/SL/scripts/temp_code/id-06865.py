import itertools

# Simulated sensor readings from a distributed environmental monitoring system
data_stream = [14, 18, 22, 19, 35, 42, 17, 25, 30, 11, 8, 50, 53, 20, 23]

# Irrelevant auxiliary data - red herring
aux_metadata = {
    'calibration_offset': 3.14159,
    'last_sync': '2023-08-01',
    'device_count': 7,
    'version': '2.1.0'
}

# Decoy transformation - never used in actual computation path
def transform_legacy(data):
    return [x * 1.05 - 2 for x in data if x > 15]

# Unused helper with misleading name
def compute_thermal_index(values):
    return sum(v ** 0.8 for v in values) / len(values)

# Real processing begins here
baseline = 20
noise_floor = 10

# Step 1: Filter out noise and extreme outliers (simultaneous high/low rejection)
filtered_data = []
for reading in data_stream:
    if noise_floor <= reading <= 52:  # Valid range
        filtered_data.append(reading)

# Distractor list comprehension - computes but unused
spike_flags = [1 if abs(filtered_data[i] - filtered_data[i-1]) > 10 else 0 
                for i in range(1, len(filtered_data))]

# Threshold function factory - relevant
create_dynamic_threshold = lambda base, sensitivity: lambda x: x > (base + sensitivity)

# Misleading intermediate function - looks important but unused
get_aggregate_stats = lambda data: {
    'mean': sum(data) / len(data),
    'variance': sum((x - sum(data)/len(data))**2 for x in data) / len(data),
    'peaks': len([x for x in data if x > 30])
}

# Actual threshold logic
threshold_func = create_dynamic_threshold(baseline, 5)

# Simulated fault mask - irrelevant but plausible
fault_mask = list(itertools.cycle([True, False, False]))
fault_filtered = [v for v, m in zip(filtered_data, fault_mask) if m]

# Diagnostic processing core
status_codes = []
for val in filtered_data:
    if threshold_func(val):
        status_codes.append(2)  # High alert
    elif val > baseline - 5:
        status_codes.append(1)  # Normal
    else:
        status_codes.append(0)  # Low warning

# Red herring: complex-looking but unused state tracking
class StateTracker:
    def __init__(self):
        self.history = []
        self.alert_cooldown = 0
    
    def update(self, code):
        self.history.append(code)

tracker = StateTracker()
for code in status_codes:
    tracker.update(code)  # Never used again

# Real final computation
alert_weight_map = {0: -1.0, 1: 0.5, 2: 1.8}
weighted_score = sum(alert_weight_map[code] for code in status_codes)

# Secondary adjustment based on trend
if len(filtered_data) > 1:
    increasing_trend = sum(
        1 for i in range(1, len(filtered_data)) 
        if filtered_data[i] > filtered_data[i-1]
    )
    trend_factor = increasing_trend / (len(filtered_data) - 1)
    weighted_score *= (1 + trend_factor * 0.1)

# Final diagnostic calculation - this is the key statement
final_diagnostic = int(round(weighted_score * 100))

# Dead code path - never executed
if __debug__:
    import sys
    sys.exit("Debug mode detected")

# Output the target result
print(f"Result: {final_diagnostic}")