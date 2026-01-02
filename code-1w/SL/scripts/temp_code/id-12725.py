import math

# Sensor simulation parameters (distraction: irrelevant to final result)
sensor_count = 16
sampling_rate = 2048
noise_floor = 0.003
baseline_offset = -0.0001

def generate_noise(length):
    # Dead function - never called in execution path
    return [math.sin(i * 0.1) * noise_floor for i in range(length)]

def preprocess_signal(raw_data, factor=1.0):
    # Distractor transformation - not used in main logic
    return [x * factor + baseline_offset for x in raw_data if x > 0.01]

def filter_outliers(data, limit=3):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    # Returns filtered data but actual logic uses raw counts
    return [x for x in data if abs(x - mean_val) < limit * std_dev]

def compute_checksum(sequence):
    # Bit manipulation red herring
    checksum = 0
    for val in sequence:
        shifted = int(abs(val) * 1000) % 256
        checksum ^= shifted
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)
    return checksum

def evaluate_stability(metrics):
    # Unused stability analysis with misleading intermediate scores
    if len(metrics) == 0:
        return 0.0
    weighted_sum = sum(i * val for i, val in enumerate(metrics, 1))
    norm_factor = sum(i for i in range(1, len(metrics)+1))
    return weighted_sum / norm_factor if norm_factor else 0.0

def accumulate_diagnostics(readings):
    # Real processing begins here — accumulates based on thresholds
    counts = {"critical": 0, "warning": 0, "normal": 0}
    thresholds = {"warning": 0.75, "critical": 1.5}
    
    for reading in readings:
        if reading > thresholds["critical"]:
            counts["critical"] += 1
        elif reading > thresholds["warning"]:
            counts["warning"] += 1
        else:
            counts["normal"] += 1
    
    # Secondary transformation: derive adjusted index
    adjustment = (counts["warning"] // 2) - (counts["critical"] * 3)
    base_index = counts["normal"] + adjustment
    
    # Decoy use of list comprehension (partially relevant)
    scaled_values = [v * 0.1 for v in counts.values() if v > 0]
    
    # Key derived metric (not yet final)
    temp_score = int((base_index * 100) + sum(scaled_values))
    
    return temp_score, counts

def analyze_readings(data, levels):
    # Main entry point with nested logic and distractions
    
    # Irrelevant pre-checks
    if not data or len(data) < 5:
        return -999
    
    # Real logic: count how many cross any threshold
    total_exceedances = 0
    for val in data:
        for level in sorted(levels.values(), reverse=True):
            if val > level:
                total_exceedances += 1
                break  # Count only once per value
    
    # Additional signal quality check (unused branch)
    quality_flag = True
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) > 2.0:
            quality_flag = False
            break
    
    # Core calculation chain
    raw_sum = sum(data)
    valid_range_count = sum(1 for x in data if 0.2 <= x <= 1.8)  # Relevant filtering
    
    # List comprehension with side relevance
    boosted = [x * 1.2 for x in data if x < 1.0]
    bonus_points = len(boosted) // 4
    
    # Primary accumulator
    score_component = raw_sum * valid_range_count
    
    # Apply conditional modifiers using boolean logic chain
    modifier = 1
    if total_exceedances > 10:
        modifier *= 0.8
    elif total_exceedances > 5:
        modifier *= 0.9
    else:
        modifier *= 1.1
    
    if valid_range_count > 15 and len(data) > 20:
        modifier *= 1.05

    intermediate = score_component * modifier + bonus_points

    # Final mapping through discrete cases (key step)
    if intermediate > 1200:
        category_value = 4
    elif intermediate > 800:
        category_value = 3
    elif intermediate > 400:
        category_value = 2
    else:
        category_value = 1

    # Final diagnostic computed from category and bit-adjusted checksum
    checksum_seed = int(sum(data) % 10)
    final_bitwise = (category_value << 2) ^ checksum_seed

    return final_bitwise

# Simulated sensor readings — deterministic input
raw_sensor_log = [
    0.32, 0.41, 0.76, 0.89, 1.05, 1.34, 1.67, 0.23, 0.51, 0.92,
    1.11, 1.42, 0.63, 0.77, 0.95, 1.28, 1.51, 0.44, 0.83, 0.69,
    1.01, 1.39, 1.72, 0.52, 0.87, 0.73, 1.19, 1.56, 0.38, 0.94
]

# Unused preprocessing (distractor)
filtered_data = filter_outliers(raw_sensor_log)
cleaned_signal = preprocess_signal(raw_sensor_log, factor=1.05)

# Actual used data path
processed_data = raw_sensor_log[:]  # Copy for clarity

threshold_levels = {"low": 0.5, "warning": 0.75, "high": 1.25, "critical": 1.5}

# Secondary unused diagnostics
temp_diagnostic, count_breakdown = accumulate_diagnostics(processed_data)
dummy_checksum = compute_checksum(processed_data)
stability_metric = evaluate_stability([0.1, 0.3, 0.2, 0.5, 0.7])

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_levels)

print(f"Target result: {final_diagnostic}")