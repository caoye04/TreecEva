import math

# Irrelevant constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = False

# Sensor metadata (mostly irrelevant)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
calibration_offsets = {'S1': 0.12, 'S2': -0.05, 'S3': 0.08, 'S4': 0.0}
active_sensors = sensor_ids[:3]

# Real input data for processing
raw_readings = [
    [18.2, 19.1, 18.9, 19.3, 19.0, 19.2, 19.4, 19.6],
    [20.1, 20.3, 20.0, 20.5, 20.7, 20.6, 20.8, 20.9],
    [21.5, 21.7, 21.6, 21.8, 21.9, 22.0, 22.2, 22.4],
    [17.8, 17.9, 18.0, 18.2, 18.1, 18.3, 18.5, 18.6]
]

# Decoy function - looks important but unused
def analyze_sensor_variance(data):
    variances = []
    for series in data:
        mean = sum(series) / len(series)
        variance = sum((x - mean) ** 2 for x in series) / len(series)
        variances.append(variance)
    return variances

# Another red herring: complex but dead-end transformation
transformed_logs = []
for i, log in enumerate(raw_readings):
    shifted = [x + calibration_offsets.get(f'S{i+1}', 0) for x in log]
    smoothed = [sum(shifted[j:j+3]) / 3 for j in range(len(shifted)-2)]
    transformed_logs.append(smoothed)

# Unused intermediate result (misleading)
total_smoothing_weight = sum(sum(log) for log in transformed_logs)

# Key data slicing: extract only segment from third sensor, middle portion
segment_data = raw_readings[2][2:6]  # Relevant: [21.6, 21.8, 21.9, 22.0]

# Distractor variables
baseline_reference = sum(raw_readings[0][:4]) / 4
aggregated_checksum = 0
for idx, val in enumerate(segment_data):
    aggregated_checksum += int(val) * (idx + 1)

# Simulated time intervals (unused but plausible)
time_intervals = [0.0, 0.5, 1.0, 1.5, 2.0]
delta_t = [time_intervals[i] - time_intervals[i-1] for i in range(1, len(time_intervals))]

# Real computation function (uses bit manipulation and accumulation)
def calculate_thermal_integral(data_slice):
    # Simulate physical heat integration with artificial scaling
    base_integral = 0.0
    for temp in data_slice:
        # Apply non-linear response curve (logarithmic sensitivity)
        response_factor = math.log(temp + 5)  # Prevent log(0)
        adjusted = temp * response_factor
        
        # Bit-level noise filtering simulation (neutral effect, but looks complex)
        shifted = int(adjusted * 100)
        filtered = (shifted >> 2) << 2  # Clear last 2 bits
        base_integral += filtered / 100.0
    
    # Accumulation with correction factor
    correction_flag = len(data_slice) & 1  # Always 0 for even length
    if correction_flag:
        base_integral *= 0.95
    else:
        base_integral *= 1.05  # Applies here
    
    # Additional fake path (never taken)
    if DEBUG_MODE and base_integral < 0:
        return -base_integral
        
    return base_integral

# Critical assignment - this is the key statement
thermal_capacity = calculate_thermal_integral(segment_data)

# Print final target result
print(f"Result: {thermal_capacity}")