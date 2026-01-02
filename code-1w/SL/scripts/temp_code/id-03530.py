import itertools

# Simulate sensor signal processing with noise filtering and pattern detection
def analyze_signal_strength(raw_readings):
    baseline = sum(raw_readings) / len(raw_readings)
    adjusted_readings = [x - baseline for x in raw_readings]
    squared_energy = [x ** 2 for x in adjusted_readings]
    avg_power = sum(squared_energy) / len(squared_energy)
    return avg_power


def extract_peaks(signal, min_magnitude):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] >= min_magnitude:
            peaks.append((i, signal[i]))
    # Irrelevant transformation (distractor)
    peak_strings = [f'Peak@{pos}' for pos, val in peaks]
    ''.join(peak_strings).upper()  # Dead computation
    return [val for pos, val in peaks]


def compress_data(sequence):
    # Run-length encoding (not directly used in final result)
    compressed = []
    for key, group in itertools.groupby(sequence):
        count = len(list(group))
        compressed.append((key, count))
    size_reduction = len(sequence) - len(compressed)
    return compressed, size_reduction

# Main data processing pipeline
raw_sensor_data = [12, 15, 15, 20, 20, 20, 18, 16, 22, 22, 25, 24, 23, 23, 23]
noise_floor = 17

# Filter data above noise floor
filtered_data = [x for x in raw_sensor_data if x > noise_floor]

# Compute derived metrics (some are distractions)
dynamic_range = max(filtered_data) - min(filtered_data)
energy_level = analyze_signal_strength(filtered_data)
signature_peaks = extract_peaks(filtered_data, min_magnitude=20)

temp_compression, savings = compress_data(filtered_data)
efficiency_ratio = savings / len(raw_sensor_data) if raw_sensor_data else 0

# Apply correction factor based on peak distribution
if len(signature_peaks) > 2:
    correction_factor = 0.9
else:
    correction_factor = 1.1

# Simulate calibration offset from device log (irrelevant but plausible)
device_log = "CAL:001:INIT CAL:002:RUN CAL:003:END"
calibration_events = device_log.count("CAL:")
log_checksum = sum([int(x.split(':')[1]) for x in device_log.split() if x.startswith('CAL:')]) % 100

# Key intermediate computation
threshold = int(energy_level * correction_factor) + 5

# Introduce string-based distractor
status_flags = ['OK' if x > threshold else 'LOW' for x in filtered_data]
valid_count = status_flags.count('OK')

# Core logic that determines final output
def process_signals(data, thresh):
    count_above = sum(1 for x in data if x > thresh)
    total_contribution = sum(x for x in data if x > thresh)
    if count_above == 0:
        return 0
    average_surplus = total_contribution // count_above  # Integer division
    
    # Additional logic path with dead branch
    if average_surplus < 10:
        multiplier = 2
    elif average_surplus < 20:
        multiplier = 3
    else:
        multiplier = 4  # This will be taken
    
    # Final transformation
    result = average_surplus * multiplier
    
    # Unused side calculation (distractor)
    outlier_ratio = len([x for x in data if x > thresh * 1.5]) / len(data) if data else 0
    
    return result

# Critical execution point
final_output = process_signals(filtered_data, threshold)
print(f"Target result: {final_output}")