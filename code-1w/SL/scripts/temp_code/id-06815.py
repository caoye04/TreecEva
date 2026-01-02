import math

# Simulated sensor readings with noise and redundancy
temperature_readings = [23.5, 24.1, 24.1, 25.3, 26.0, 23.5, 27.2, 26.0, 24.1, 28.8, 29.5]
humidity_readings = [45, 47, 45, 50, 52, 47, 55, 52, 47, 60, 63]
pressure_readings = [1013, 1015, 1013, 1018, 1020, 1015, 1022, 1020, 1015, 1025, 1028]

# Irrelevant transformation: historical baseline shift (unused)
historical_offset = 0.7
legacy_baseline_temps = [round(t - historical_offset, 2) for t in temperature_readings]

# Misleading aggregation: average drift (dead path)
avg_temp_drift = sum([temperature_readings[i+1] - temperature_readings[i] for i in range(len(temperature_readings)-1)]) / 10

# Core data fusion pipeline
raw_data_pool = []
for i in range(len(temperature_readings)):
    raw_data_pool.append((
        round(temperature_readings[i] + 273.15),  # Kelvin conversion
        humidity_readings[i] + 10,                    # Artificial bias
        pressure_readings[i] % 100                   # Normalize pressure
    ))

# Distractor: secondary correlation analysis (never used)
correlation_proxy = 0
for temp_k, hum_b, press_norm in raw_data_pool:
    if hum_b > 50 and press_norm < 30:
        correlation_proxy += temp_k * 0.1

# Real processing begins: extract unique thermal states
thermal_states = {item[0] for item in raw_data_pool}  # Set removes duplicates

# Filtering condition based on environmental thresholds
valid_states = set()
threshold_pressure = 25
for state in thermal_states:
    # Find corresponding entry
    for item in raw_data_pool:
        if item[0] == state:
            if item[2] > threshold_pressure:  # Only high-normalized pressure
                valid_states.add(state)
            break

# Simulate compression via dimensionality reduction
compression_iterations = 0
working_set = valid_states.copy()
reduction_factor = 0.9
while len(working_set) > 3 and compression_iterations < 5:
    sorted_vals = sorted(working_set)
    # Remove every second element (simulated compression)
    pruned = {sorted_vals[i] for i in range(0, len(sorted_vals), 2)}
    working_set = pruned
    compression_iterations += 1

# Decoy clustering algorithm (unused result)
cluster_centers = []
sorted_working = sorted(working_set)
for i in range(0, len(sorted_working) - 1, 2):
    center = (sorted_working[i] + sorted_working[i+1]) / 2
    cluster_centers.append(center)

# Final optimization: remove outliers beyond 3-sigma equivalent
mean_val = sum(working_set) / len(working_set)
variance = sum((x - mean_val) ** 2 for x in working_set) / len(working_set)
std_dev = math.sqrt(variance)
three_sigma_high = mean_val + 3 * std_dev
efficient_set = {x for x in working_set if x <= three_sigma_high}

# Key computation chain
baseline_compression = 4.0
compression_ratio = baseline_compression * (1 + 0.1 * compression_iterations)

# Secondary irrelevant normalization
normalization_lut = {k: k / sum(efficient_set) for k in efficient_set}

# Dead-end diagnostic check
if len(efficient_set) % 2 == 0:
    diagnostic_flag = sum(normalization_lut.values()) > 1.0
else:
    diagnostic_flag = False

# High-interference red herring: recursive checksum (unused)
def calculate_recursive_checksum(data, depth=0):
    if depth >= 3 or len(data) == 1:
        return list(data)[0] % 7
    sorted_data = sorted(data)
    half = len(sorted_data) // 2
    left = set(sorted_data[:half])
    right = set(sorted_data[half:])
    return (calculate_recursive_checksum(left, depth+1) ^ 
            calculate_recursive_checksum(right, depth+1))

checksum_herring = calculate_recursive_checksum(valid_states)

# Actual target computation
optimized_set = efficient_set.intersection(thermal_states).difference({min(thermal_states)})

# Critical statement
filtration_score = len(optimized_set) * compression_ratio

print(f"Result: {filtration_score}")