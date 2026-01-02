import math

# Simulated sensor network data processing with diagnostic analysis
def collect_raw_readings():
    return [23.4, 18.9, 25.1, 30.2, 17.8, 22.0, 26.5, 29.8, 20.3, 24.7]

def apply_calibration(raw_values, factor=1.02, offset=-0.5):
    # Real calibration logic
    return [(v * factor) + offset for v in raw_values]

def filter_outliers(data, low_bound=18.0, high_bound=30.0):
    # Remove values outside acceptable physical range
    filtered = [v for v in data if low_bound <= v <= high_bound]
    return filtered if len(filtered) > 2 else data[:len(data)//2 + 1]

def compute_rolling_average(values, window=3):
    # Smooth data using rolling average
    smoothed = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        smoothed.append(sum(values[start:i+1]) / (i - start + 1))
    return smoothed

def generate_checksum(sequence):
    # Irrelevant: used for transmission verification (distractor)
    return sum(v * (i+1) for i, v in enumerate(sequence)) % 1000

def encrypt_data(data):
    # Distractor function: not used in main flow
    return [round(math.sin(v/10) * 1000) for v in data]

def dummy_transformation(x):
    # Dead code path — never called
    return x ** 2 - 2*x + 1

def prepare_lookup_table():
    # Creates a red herring mapping (partially used)
    keys = ['temp', 'pressure', 'humidity']
    values = [list(range(10)), list(range(5, 15)), list(range(20, 30))]
    table = dict(zip(keys, values))
    table['aux_data'] = {i: chr(65 + i%26) for i in range(10)}  # Unused structure
    return table

def evaluate_stability_metric(data):
    # Misleading intermediate metric
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def aggregate_diagnostic_flags(data):
    # Real but indirect contribution to final result
    flags = set()
    if any(v > 25 for v in data):
        flags.add('high_temp_alert')
    if all(v < 28 for v in data):
        flags.add('within_operational_range')
    if len(data) > 6:
        flags.add('sufficient_sample_volume')
    return flags

def derive_threshold_map(flags, base_map=None):
    # Builds actual threshold map used in analysis
    if base_map is None:
        base_map = {'critical': 27.5, 'warning': 25.0, 'normal': 22.0}
    adjustment = 1.5 if 'high_temp_alert' not in flags else -0.8
    # Only this modified value matters
    base_map['adjusted_critical'] = base_map['critical'] + adjustment
    return base_map

def slice_critical_window(data, center_at=None):
    # Uses slicing and returns core segment
    if center_at is None:
        center_at = len(data) // 2
    start = max(0, center_at - 3)
    end = min(len(data), center_at + 4)
    return data[start:end]  # Returns up to 7 elements around center

def count_significant_exceedances(segment, thresholds):
    # Counts how many readings go above adjusted critical level
    limit = thresholds['adjusted_critical']
    return sum(1 for v in segment if v > limit)

def calculate_precision_score(exceedances, size):
    # Red herring scoring system (not used)
    return round((size - abs(exceedances - 3)) / size, 4)

def analyze_readings(processed_data, threshold_map):
    # Final decision logic
    segment = slice_critical_window(processed_data, center_at=5)
    exceedances = count_significant_exceedances(segment, threshold_map)
    stability = evaluate_stability_metric(processed_data)  # Computed but unused
    score = calculate_precision_score(exceedances, len(segment))  # Dead calculation
    flags = aggregate_diagnostic_flags(segment)  # Recomputed but only partially affects logic
    penalty = -5 if 'high_temp_alert' in flags else 0
    base_value = 100 + exceedances * 7
    final_score = base_value + penalty
    return final_score

# --- Main Execution with Distractions ---
raw_readings = collect_raw_readings()

# Apply real processing steps
calibrated = apply_calibration(raw_readings)
filtered = filter_outliers(calibrated)
smoothed = compute_rolling_average(filtered)

# Irrelevant computations (distractors)
checksum = generate_checksum(smoothed)
encrypted = encrypt_data(smoothed)
lookup_table = prepare_lookup_table()  # Created but mostly unused
stability_index = evaluate_stability_metric(smoothed)  # Used nowhere

# Partially relevant flag generation
diagnostic_flags = aggregate_diagnostic_flags(smoothed)

# Build threshold map using flags
threshold_map = derive_threshold_map(diagnostic_flags)

# Another distractor: sorting unrelated data
aux_list = [8, 1, 6, 3, 9, 2]
sorted_aux = sorted(aux_list, reverse=True)  # No impact on result

# Core data for analysis
processed_data = smoothed

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")