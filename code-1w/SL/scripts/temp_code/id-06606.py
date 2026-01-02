import math

# Simulated sensor data processing with diagnostic logic
def collect_readings():
    raw_values = [i * 1.5 + math.sin(i) for i in range(100)]
    filtered = [v for v in raw_values if v > 0]
    return filtered[:50]

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(x):
    return (x * 0.95) ** 2

# Transform data using sliding window and statistical smoothing
def smooth_signal(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window)
        segment = data[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(round(avg, 3))
    return smoothed

# Misleading normalization function that is never used
def normalize_intensity(values, factor=100.0):
    max_val = max(values)
    return [int(v / max_val * factor) for v in values]

# Data categorization based on dynamic thresholds
def classify_bands(signal):
    bands = {'low': 0, 'medium': 0, 'high': 0}
    counts = {'processed': 0, 'skipped': 0}  # Tracking metadata
    
    for val in signal:
        if val < 40:
            bands['low'] += 1
        elif val < 75:
            bands['medium'] += 1
        else:
            bands['high'] += 1
        counts['processed'] += 1
    
    return bands, counts

# Red herring: Unused pattern matcher
def detect_spike_sequence(data):
    spikes = []
    for i in range(2, len(data)):
        if data[i] > data[i-1] > data[i-2] and data[i] > 50:
            spikes.append(i)
    return len(spikes) > 5

# Core transformation: apply logarithmic scale and shift
def transform_readings(raw):
    adjusted = []
    offset = 10.5
    for x in raw:
        if x <= 0:
            adjusted.append(0)
        else:
            transformed = math.log(x) * 2.5 + offset
            adjusted.append(round(transformed, 3))
    return adjusted

# Threshold map generation - relevant for final analysis
def generate_thresholds(mode='standard'):
    base_map = {}
    for i in range(5):
        key = f'level_{i}'
        base_map[key] = (i + 1) * 3.7
    
    # Add decoy keys with misleading values
    base_map['debug_mode'] = True
    base_map['last_updated'] = '2023-01-01'
    base_map['version'] = 1.2
    
    return base_map

# Main analysis function with early returns and conditional logic
def analyze_pattern(dataset, thresholds):
    if not dataset or len(dataset) == 0:
        return -1
    
    total = 0.0
    contribution = []
    level_0_threshold = thresholds['level_0']
    level_1_threshold = thresholds['level_1']
    level_2_threshold = thresholds['level_2']
    level_3_threshold = thresholds['level_3']
    level_4_threshold = thresholds['level_4']

    for val in dataset:
        if val < level_0_threshold:
            total += val * 0.5
        elif val < level_1_threshold:
            total += val * 0.7
        elif val < level_2_threshold:
            total += val * 0.8
        elif val < level_3_threshold:
            total += val * 0.9
        elif val < level_4_threshold:
            total += val * 1.0
        else:
            total += val * 1.1

        # Early break condition based on accumulated value
        if total > 1500:
            break

    # Apply correction factor based on dictionary lookup
    adjustment_key = 'level_2'
    correction = 1.03 if thresholds[adjustment_key] > 7.0 else 0.97
    total *= correction

    # Final filtering based on length-dependent rule
    if len(dataset) % 2 == 1:
        total -= 15.25
    else:
        total += 10.75

    return round(total, 3)

# --- Execution Flow ---
# Collect initial sensor readings
sensor_data = collect_readings()

# Smooth the signal (irrelevant to final result but looks important)
dummy_smoothing = smooth_signal(sensor_data)

# Transform the data - this output is actually used
dummy_normalization = normalize_intensity(sensor_data)  # Dead call
transformed_data = transform_readings(sensor_data)

# Generate threshold map for classification
threshold_map = generate_thresholds('standard')

# Perform band classification (used to distract from main flow)
band_distribution, meta_counts = classify_bands(transformed_data)

# Detect anomalies (never called - red herring)
# spike_event = detect_spike_sequence(transformed_data)

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

print(f"Result: {final_diagnostic}")