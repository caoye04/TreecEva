import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = {0x1A, 0x2B, 0x3C, 0x4D, 0x5E}
validation_keys = {0x2B, 0x3C, 0x6F, 0x7G}
overlap_check = legacy_codes & validation_keys  # Red herring operation

# Signal processing pipeline
scaling_factor = 1.05
offset_correction = -0.8

# Apply scaling and offset to temperature (relevant)
adjusted_temps = []
for t in temperature_readings:
    adjusted_temps.append(round(t * scaling_factor + offset_correction, 2))

# Compute moving average over 3 elements (relevant)
moving_avg = []
for i in range(2, len(adjusted_temps)):
    avg = (adjusted_temps[i-2] + adjusted_temps[i-1] + adjusted_temps[i]) / 3
    moving_avg.append(round(avg, 2))

# Frequency domain transformation attempt (mostly irrelevant)
fft_magnitude = []
for val in adjusted_temps:
    transformed = abs(val * math.sin(math.pi * val / 10))
    fft_magnitude.append(round(transformed, 3))

# Noise filtering using threshold (dead code path - never used)
noise_floor = 1.25
filtered_noise = [x for x in fft_magnitude if x > noise_floor]

# Bitmask simulation for hardware compatibility (distractor)
hw_status_word = 0b11011010
error_mask = 0b00100100
masked_status = hw_status_word & ~error_mask  # Looks important but unused

# Data fusion: combine humidity and pressure into index (partially relevant)
composite_index = []
for h, p in zip(humidity_readings, pressure_readings):
    idx = (h * 0.7) + ((p - 1000) * 0.3)
    composite_index.append(round(idx, 2))

# Secondary index smoothing with conditional logic (irrelevant)
smoothed_index = []
for i, val in enumerate(composite_index):
    if i == 0:
        smoothed_index.append(val)
    else:
        diff = abs(val - smoothed_index[-1])
        if diff > 5.0:
            smoothed_index.append(smoothed_index[-1] + 5.0)
        else:
            smoothed_index.append(val)

# Processed signals used in final analysis (core relevant data)
processed_signals = []
for mt, ci in zip(moving_avg, composite_index[2:]):
    fused = mt * 0.6 + ci * 0.4
    processed_signals.append(round(fused, 2))

# Decoy function that looks diagnostic but is unused
def compute_health_score(data):
    base = sum(data) / len(data)
    penalty = 0
    for x in data:
        if x < 20:
            penalty += 5
    return max(base - penalty, 0)

# Real analysis function
def analyze_readings(signal_data):
    if not signal_data:
        return 0.0
    
    # Calculate statistical properties
    mean_val = sum(signal_data) / len(signal_data)
    variance = sum((x - mean_val) ** 2 for x in signal_data) / len(signal_data)
    std_dev = math.sqrt(variance)
    
    # Apply empirical correction factors
    corrected_mean = mean_val * 0.92 + std_dev * 1.8
    
    # Outlier trimming: exclude values beyond 2*std_dev
    lower_bound = mean_val - 2 * std_dev
    upper_bound = mean_val + 2 * std_dev
    filtered_data = [x for x in signal_data if lower_bound <= x <= upper_bound]
    
    # Recompute mean on filtered data
    final_mean = sum(filtered_data) / len(filtered_data)
    
    # Final nonlinear transformation based on calibration curve
    final_diagnostic = math.log(final_mean * 1.45 + 10)
    
    return round(final_diagnostic, 6)

# Trigger point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output requirement
print(f"Result: {final_diagnostic}")