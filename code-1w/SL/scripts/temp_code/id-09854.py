import itertools

# Sensor array diagnostics with noise filtering and calibration
raw_readings = [107, 214, 198, 255, 132, 189, 203, 176, 244, 168]
noise_floor = 150
sample_window = 3
calibration_map = {'offset': 17, 'gain': 0.88}
diagnostic_log = []
baseline_shift = 0

# Irrelevant diagnostic counters (distractors)
error_count = 0
warning_level = 0
phase_counter = 0
redundant_flag = False
temp_buffer = [0] * 5

# Simulated environmental interference (dead code path)
def apply_shield_filter(data):
    return [x for x in data if x > 100]  # Unused function

# Misleading preprocessing step (not actually used in final path)
shadow_copy = [x ^ 255 for x in raw_readings]  # Bitwise red herring
shadow_copy = [y for y in shadow_copy if y % 2 == 0]

# Real signal processing begins here
smoothed = []
for i in range(len(raw_readings) - sample_window + 1):
    window_avg = sum(raw_readings[i:i+sample_window]) / sample_window
    smoothed.append(int(window_avg))

# Filter based on dynamic threshold
adaptive_threshold = sum(smoothed) // len(smoothed) - 10
filtered_data = [x for x in smoothed if x > adaptive_threshold]

# Decoy transformation using slicing and concatenation (unused)
extended_slice = filtered_data[::2] + filtered_data[::-1][:3]
extended_slice = extended_slice[:len(extended_slice)//2]  # Partial usage distraction

# Multiple assignment red herring
calibration_factor, gain_adjust, _ = calibration_map['offset'], calibration_map['gain'], baseline_shift + 5

# Tuple unpacking with irrelevant components
primary, secondary = (calibration_factor * 2, gain_adjust * 1.1)
signal_metadata = (len(filtered_data), sum(filtered_data), primary)

# Real processing function with embedded logic
def process_readings(data, offset):
    result_chain = []
    for val in data:
        # Apply calibration offset and clamp
        calibrated = val - offset
        if calibrated < 0:
            calibrated = 0
        # Group by magnitude bands using dictionary
        band_key = calibrated // 20
        band_counts = {i: 0 for i in range(10)}
        band_counts[band_key] += 1  # Only updates once per loop - misleading use
        result_chain.append(calibrated)
    
    # Use itertools to create artificial complexity
    rolling_pairs = list(itertools.pairwise(result_chain))
    pair_sum = sum(a + b for a, b in rolling_pairs if (a + b) % 2 == 0)
    
    # Final aggregation with decoy condition
    adjustment = 0
    if len(result_chain) > 4:
        adjustment = len([x for x in result_chain if x > 30]) * 2
    return pair_sum + adjustment

# Critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Print result as required
print(f"Result: {final_diagnostic}")