from collections import defaultdict, Counter

# Irrelevant sensor calibration data (distractor)
calibration_offsets = [0.12, -0.05, 0.33, 0.0, 0.18, -0.11]
sensor_noise_floor = sum([abs(x) for x in calibration_offsets]) / len(calibration_offsets)

# Simulated efficiency readings over time (core input)
efficiency_readings = [
    87.3, 92.1, 88.4, 95.6, 90.2, 85.0, 93.8, 89.7, 91.5, 86.9,
    94.2, 88.0, 90.1, 87.6, 92.3, 89.4, 91.0, 90.8, 86.5, 93.1
]

# Auxiliary metadata (mostly irrelevant)
device_id_mapping = defaultdict(lambda: 'UNKNOWN')
device_id_mapping.update({i: f'DEV-{1000+i}' for i in range(len(efficiency_readings))})

# Phantom system status tracker (red herring)
system_health_flags = []
for val in efficiency_readings:
    if val > 92.0:
        system_health_flags.append('OPTIMAL')
    elif val > 88.0:
        system_health_flags.append('STABLE')
    else:
        system_health_flags.append('MONITORING')

# Decoy function that looks important but is unused
def calculate_reliability_score(data):
    weighted_sum = 0
    for i, x in enumerate(data):
        weighted_sum += x * (0.9 ** i)
    return round(weighted_sum / len(data), 3)

# Fake diagnostic routine (dead code path)
def run_diagnostics(mode='standard'):
    if mode == 'deep':
        return {"errors": 0, "warnings": 5, "status": "OK"}
    return {"errors": 0, "warnings": 0, "status": "OK"}

# Real processing begins here
threshold = 89.5

# Filter and transform efficiency data
filtered_readings = [x for x in efficiency_readings if x >= threshold]

# Compute moving average over 3-point window (unused distractor)
moving_avg = []
for i in range(2, len(efficiency_readings)):
    moving_avg.append(round(sum(efficiency_readings[i-2:i+1]) / 3, 2))

# Count frequency bands (semi-relevant, used later)
frequency_counter = Counter()
for val in efficiency_readings:
    band = int(val // 5) * 5  # group by 5-unit intervals
    frequency_counter[band] += 1

# Secondary transformation: normalize filtered values to percentage above threshold
deviations = [(val - threshold) / threshold * 100 for val in filtered_readings]

# Simulate thermal load accumulation with decay factor
thermal_load = 0.0
decay_factor = 0.88
for i, dev in enumerate(deviations):
    weight = decay_factor ** i
    thermal_load += dev * weight

# Auxiliary string manipulation (distractor)
log_header = "EFFICIENCY_METRICS_V2"
header_checksum = sum(ord(c) for c in log_header if c.isalpha()) % 100

# Another decoy structure (irrelevant list slicing)
rotated_slice = efficiency_readings[5:] + efficiency_readings[:5]
inverted_peak = max(rotated_slice[::2])  # misleading peak detection

# Core logic wrapped in a function
def process_thermal_metrics(data, min_threshold):
    # Re-filter inside function (redundant but realistic)
    active_entries = [x for x in data if x >= min_threshold]
    
    # Unrelated sorting operation (distractor)
    sorted_desc = sorted(active_entries, reverse=True)
    median_value = sorted_desc[len(sorted_desc)//2]
    
    # Bit manipulation mask based on length (red herring)
    mask = len(active_entries) ^ 255
    masked_sum = sum(active_entries) ^ mask  # decoy calculation
    
    # Actual metric computation
    base_metric = sum(active_entries) / len(active_entries)
    adjustment_factor = len(frequency_counter) / 10.0  # uses earlier counter
    capacity_score = (base_metric * adjustment_factor) + (thermal_load / 100)
    
    # Final nonlinear scaling
    import math
    scaled_capacity = math.log(capacity_score) * math.pi
    
    return round(scaled_capacity, 6)

# Key execution point
thermal_capacity = process_thermal_metrics(efficiency_readings, threshold)

# Print result as required
print(f"Target result: {thermal_capacity}")