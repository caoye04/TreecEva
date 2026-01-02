import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    raw_values = [127, 255, 193, 64, 89, 211]
    scaling_factor = 0.75
    adjusted = [v * scaling_factor for v in raw_values]
    return adjusted

# Irrelevant preprocessing - red herring
def normalize_signal(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Distractor function - never called in execution path
def legacy_calibrate(arr):
    return [int(x * 1.1) for x in arr if x > 50]

# Real processing begins here
def filter_outliers(values, limit=75.0):
    return [v for v in values if v > limit]

# Bit manipulation for checksum simulation
def compute_checksum(num_list):
    checksum = 0
    for val in num_list:
        int_val = int(val)
        checksum ^= int_val  # XOR into checksum
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)  # Rotate left
    return checksum

# Recursive smoothing function (actual use)
def smooth_recursive(vals, idx=0):
    if idx >= len(vals) - 1:
        return [vals[idx]]
    smoothed = [(vals[idx] + vals[idx+1]) / 2]
    return smoothed + smooth_recursive(vals, idx + 1)

# Set-based interference: irrelevant diagnostic modes
def generate_diagnostics():
    modes = {'thermal', 'pressure', 'flow', 'vibration'}
    alerts = {'pressure', 'flow'}
    pending = {'flow', 'humidity'}
    # Meaningless set operations as distractors
    active = (modes & alerts) | pending
    inactive = modes - active
    priority = {x.upper() for x in active.intersection(alerts)}
    return list(priority)  # Never used

def accumulate_trend(data):
    trend_sum = 0.0
    for i in range(1, len(data)):
        trend_sum += (data[i] - data[i-1]) * 0.5
    return trend_sum

# Main analysis with key logic
threshold_set = {60, 75, 90, 100}
def analyze_readings(data, thresholds):
    # Step 1: Filter using threshold set membership
    valid_entries = [x for x in data if x > min(thresholds)]
    
    # Step 2: Recursive smoothing
    smoothed = smooth_recursive(valid_entries)
    
    # Step 3: Accumulate trend
    trend = accumulate_trend(smoothed)
    
    # Step 4: Compute checksum on original filtered ints
    check = compute_checksum([int(x) for x in valid_entries])
    
    # Step 5: Apply decay factor based on set size
    decay = len(thresholds) * 0.1
    
    # Step 6: Combine results into diagnostic score
    raw_diagnostic = trend * decay + check
    
    # Step 7: Spurious correction (looks important but fixed)
    corrections = {"alpha": 0.95, "beta": 1.05, "gamma": 0.0}  # gamma never used
    final_diagnostic = raw_diagnostic * corrections["alpha"]
    
    return final_diagnostic

# Unused variables - dead code paths
baseline_profile = [0.1, 0.25, 0.5]
calibration_matrix = [[1,0],[0,1]]
redundant_flag = False
aux_data = set()

# Execution flow
sensor_log = collect_readings()
filtered_data = filter_outliers(sensor_log)
normalized = normalize_signal(filtered_data)  # Computed but not used
processed_data = [math.sqrt(x) for x in filtered_data]  # Key transformation

# Irrelevant recursive depth counter
recursion_trace = []

def track_depth(n, depth=0):
    if n <= 1:
        recursion_trace.append(depth)
        return
    track_depth(n // 2, depth + 1)

def run_self_test():
    for val in [128, 64, 32]:
        track_depth(val)

run_self_test()  # Fills trace but unused

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_set)
print(f"Result: {final_diagnostic}")