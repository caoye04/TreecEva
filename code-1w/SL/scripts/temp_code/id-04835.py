from collections import defaultdict, Counter

# Simulated sensor data ingestion and preprocessing
def preprocess_sensor_array(raw_readings):
    normalized = []
    for val in raw_readings:
        if val < 0:
            val = abs(val) % 100
        normalized.append(round(val ** 0.5, 3))
    return normalized

# Feature engineering pipeline
def extract_engineered_features(processed):
    engineered = []
    temp_store = defaultdict(int)
    
    for i, x in enumerate(processed):
        temp_store[i] += int(x * 10)
        if i % 2 == 0:
            engineered.append(x * 1.5)
        else:
            engineered.append(x * 0.8)
    
    # Irrelevant aggregation (distractor)
    avg_temp = sum(temp_store.values()) / len(temp_store) if temp_store else 0
    spike_count = sum(1 for v in processed if v > 5)
    
    return engineered

# Legacy compatibility layer (mostly dead code path)
def legacy_compatibility_mode(data, mode='basic'):
    if mode == 'advanced':
        return [d * 0.95 for d in data]
    elif mode == 'debug':
        checksum = 0
        for d in data:
            checksum = (checksum + d * 3) % 97
        return [checksum] * len(data)
    else:
        return data  # default fallback

# Baseline calibration with red herring computations
def calculate_baseline_adjustment(signal):
    base_ref = [s % 7 for s in signal]
    adjusted = []
    
    magnitude = sum(b ** 2 for b in base_ref) ** 0.5
    scale_factor = 1.0 if magnitude == 0 else 10 / magnitude
    
    for b in base_ref:
        transformed = (b * scale_factor) + 0.1
        adjusted.append(transformed)
    
    # Decoy metrics (irrelevant to final result)
    outlier_flags = [1 if a > 5 else 0 for a in adjusted]
    penalty_score = sum(outlier_flags) * 0.05
    
    return adjusted

# Main diagnostic workflow
raw_sensor_data = [85, -23, 64, 144, -9, 25, 169, 49, 121, 36]

# Step 1: Normalize readings
cleaned_signal = preprocess_sensor_array(raw_sensor_data)

# Step 2: Extract high-level features
engineered_features = extract_engineered_features(cleaned_signal)

# Step 3: Compute baseline reference (used later)
baseline = calculate_baseline_adjustment(cleaned_signal)

# Step 4: Simulate compression factor from metadata (key value)
metadata_frame = zip(['len', 'ver', 'cid'], [10, 3, 4852])
frame_dict = dict(metadata_frame)
compression_factor = frame_dict['cid'] % 7  # evaluates to 3

# Step 5: Aggregate metrics using combined feature set
aggregate_metrics = lambda f1, f2: sum(f1[i] * f2[i] for i in range(len(f1)))

# Step 6: Apply final diagnostic computation
final_diagnostic = aggregate_metrics(engineered_features, baseline) // compression_factor

# Distraction block: unused analysis paths
unused_correlation = Counter()
for x, y in zip(engineered_features, baseline):
    key = round(x, 1)
    unused_correlation[key] += 1

debug_snapshot = [cleaned_signal[i] for i in range(0, len(cleaned_signal), 2)]
temp_correction = sum(baseline) / sum(cleaned_signal) if sum(cleaned_signal) != 0 else 0

# Final output
print(f"Result: {final_diagnostic}")