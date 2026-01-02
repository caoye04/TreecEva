import math

# Irrelevant sensor calibration data (red herring)
sensor_offsets = [0.12, -0.05, 0.33, 0.08, -0.17]
baseline_readings = {i: math.sin(i * 0.5) for i in range(10)}

# Decoy function - looks important but unused
def deprecated_calibrate(x):
    return sum([math.tanh(val + x) for val in sensor_offsets])

# Unused transformation pipeline
transform_chain = [
    lambda x: x ** 2,
    lambda x: x + 1e-6,
    lambda x: math.log(max(x, 1e-9))
]

# Real data processing begins here
raw_metrics = [18, 24, 42, 56, 29, 33, 41, 19]

# Misleading intermediate calculation (dead path)
temp_normalization = 0
for val in raw_metrics:
    if val > 30:
        temp_normalization += math.sqrt(val) * 0.1

# Another decoy: complex-looking but unused formula
redundant_factor = sum(math.cos(i) ** 2 + math.sin(i) ** 2 for i in range(5))  # Always 5.0

# Actual signal extraction via slicing and filtering
filtered_deltas = raw_metrics[1::2]  # Take odd indices: [24, 56, 33, 19]
adjusted_peaks = [x - 10 for x in filtered_deltas if x > 20]

# Simulated time-series window analysis (only some used)
window_size = 3
sliding_windows = [
    adjusted_peaks[i:i+window_size] 
    for i in range(len(adjusted_peaks) - window_size + 1)
]

# Key function that uses lambda and actual logic
integrate_window = lambda win: sum(w * (i+1) for i, w in enumerate(win))

aggregated_response = 0
if len(sliding_windows) > 0:
    weighted_windows = [integrate_window(window) for window in sliding_windows]
    aggregated_response = max(weighted_windows)  # Only this matters

# Fake feedback loop with no effect
feedback_signal = 0
for _ in range(3):
    feedback_signal = math.atan(feedback_signal + 0.1)

# Core logic hidden among distractions
def calculate_efficiency(data):
    base = len(data) * 2
    shift = data[0] // 4
    return base + shift - 7

profile_data = [aggregated_response, 88, 12, 99, 44]  # First element is key

# Critical statement — answer depends on this
thermal_capacity = calculate_efficiency(profile_data)

# Output required format
print(f"Target result: {thermal_capacity}")