import math

# Simulated sensor readings with noise
temperature_readings = [23.4, 19.5, 27.2, 30.1, 18.9, 22.0, 25.3, 29.8, 17.6, 24.1]

# Irrelevant auxiliary data (distractor)
pressure_readings = [101.3, 99.7, 102.1, 100.5, 98.9, 103.2, 101.8, 97.6, 100.0, 102.5]
humidity_readings = [45, 48, 52, 60, 44, 50, 58, 62, 41, 47]

# Noise threshold and calibration factor (some are decoys)
calibration_factor = 1.05
noise_floor = 0.5
scaling_constant = 2.718  # Unused red herring (looks important)

# Step 1: Apply calibration to temperature (relevant)
calibrated_temps = [t * calibration_factor for t in temperature_readings]

# Step 2: Detect anomalies using moving average (partially relevant)
anomaly_flags = []
moving_avg_window = 3
for i in range(len(calibrated_temps)):
    if i < moving_avg_window:
        window_avg = sum(calibrated_temps[:i+1]) / (i+1)
    else:
        window_avg = sum(calibrated_temps[i-moving_avg_window+1:i+1]) / moving_avg_window
    deviation = abs(calibrated_temps[i] - window_avg)
    anomaly_flags.append(deviation > 2.0)

# Step 3: Transform data by squaring non-anomalous values (relevant)
transformed_data = []
for i, temp in enumerate(calibrated_temps):
    if not anomaly_flags[i]:
        transformed_data.append(temp ** 2)
    else:
        transformed_data.append(0)  # Anomalous points zeroed out

# Dead function - looks useful but never called (distractor)
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        if i == 0:
            smoothed.append((signal[0] + signal[1]) / 2)
        elif i == len(signal) - 1:
            smoothed.append((signal[-1] + signal[-2]) / 2)
        else:
            smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    return smoothed

# Another decoy function with misleading name (never used)
def normalize_range(data, min_val=0, max_val=100):
    actual_min = min(data)
    actual_max = max(data)
    return [(x - actual_min) / (actual_max - actual_min) * (max_val - min_val) + min_val for x in data]

# Step 4: Process the transformed data to extract filtered sum (key logic)
def process_data(data):
    # Filter out zeros (originally anomalous)
    non_zero_vals = [x for x in data if x > 0]
    
    # Sort and take top half (if even count)
    sorted_vals = sorted(non_zero_vals, reverse=True)
    cutoff = len(sorted_vals) // 2
    top_half = sorted_vals[:cutoff] if cutoff > 0 else sorted_vals
    
    # Apply logarithmic weighting (only if value > 500)
    weighted_vals = []
    for val in top_half:
        if val > 500:
            weighted_vals.append(math.log(val) * 10)
        else:
            weighted_vals.append(val * 0.1)  # Minor contribution
    
    # Compute final metrics (only one returned)
    total_energy = sum(weighted_vals)
    peak_value = max(weighted_vals) if weighted_vals else 0
    filtered_sum = int(sum(top_half))  # Critical answer variable
    
    # Return only one, but others look plausible
    return total_energy  # Misdirection!

# Execution point of interest
final_result = process_data(transformed_data)

# Extract the real target variable that was computed inside the function
# We reconstruct it externally to avoid returning it directly
non_zero_vals_ext = [x for x in transformed_data if x > 0]
sorted_vals_ext = sorted(non_zero_vals_ext, reverse=True)
cutoff_ext = len(sorted_vals_ext) // 2
top_half_ext = sorted_vals_ext[:cutoff_ext] if cutoff_ext > 0 else sorted_vals_ext
filtered_sum = sum(top_half_ext)

print(f"Result: {filtered_sum}")