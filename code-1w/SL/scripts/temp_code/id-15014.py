import math

# Simulated sensor fusion system for environmental monitoring
def collect_readings():
    raw_data = [23.4, 25.1, 24.8, 19.2, 26.7, 24.3, 1024, 25.0, 23.9]
    baseline = 24.5
    deviation_threshold = 1.5
    high_range_offset = 1000
    scaling_factor = 0.98
    adjusted = [(x - baseline) * scaling_factor for x in raw_data if x < high_range_offset]
    return adjusted

def filter_anomalies(readings):
    clean_set = set()
    temp_buffer = []
    anomaly_count = 0
    
    for val in readings:
        if abs(val) > 2.0:
            anomaly_count += 1
            continue
        temp_buffer.append(val)
    
    # Simulate redundant filtering (distractor)
    if len(temp_buffer) > 5:
        smoothed = [temp_buffer[i] for i in range(len(temp_buffer)) if i % 2 == 0]
    else:
        smoothed = temp_buffer
    
    # Use set to eliminate duplicates (core operation)
    clean_set.update(smoothed)
    
    # Irrelevant transformations
    shadow_copy = [x * -1 for x in temp_buffer]
    inversion_check = sum(1 for x in shadow_copy if x > 0)
    dummy_aggregate = inversion_check * 0.5 if inversion_check > 0 else 0
    
    return list(clean_set)

def compute_entropy(values):
    # Dead function - never called but looks important
    if not values:
        return 0.0
    total = sum(abs(x) for x in values)
    if total == 0:
        return 0.0
    return -sum((abs(x)/total) * math.log(abs(x)/total) for x in values if x != 0)

def rolling_window_avg(data, window=3):
    # Unused helper with misleading relevance
    if len(data) < window:
        return [0.0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def analyze_readings(processed):
    # Core analysis logic
    if not processed:
        return -999
    
    # Key intermediate variables
    magnitude_sum = sum(abs(x) for x in processed)
    sign_distribution = {'positive': 0, 'negative': 0}
    for x in processed:
        if x >= 0:
            sign_distribution['positive'] += 1
        else:
            sign_distribution['negative'] += 1
    
    balance_ratio = (sign_distribution['positive'] + 1) / (sign_distribution['negative'] + 1)
    
    # Secondary processing chain (distraction)
    squared_chain = [x**2 for x in processed]
    cumulative_decay = 0.0
    decay_rate = 0.85
    for sq in squared_chain:
        cumulative_decay = cumulative_decay * decay_rate + sq * (1 - decay_rate)
    
    # Red herring: complex-looking transformation
    phantom_metric = math.sqrt(cumulative_decay) * math.cos(len(processed))
    temporal_weight = sum(i * v for i, v in enumerate(processed))  # Unused
    
    # Critical decision point
    if magnitude_sum < 1.0:
        return 0
    elif balance_ratio > 2.0:
        return int(magnitude_sum * 100)
    else:
        # Final result path
        base_score = magnitude_sum * 1000
        adjustment = (len(processed) * 50) // (int(balance_ratio) + 1)
        return int(base_score - adjustment)

# Global configuration (mostly irrelevant)
SYSTEM_ID = "ENV-SENSE-ALPHA"
CALIBRATION_MODE = False
LOGGING_INTERVAL = 15
TEMPORAL_SNAPSHOT = [0.1, 0.2, 0.3]
ANALYSIS_WINDOW = (0, 100)
VERSION_TAG = "v2.1.5"
DEBUG_FLAGS = {"io_trace": False, "memory_profile": False, "timing_snapshots": False}

# Primary execution flow
raw_sensor_cluster = collect_readings()
sanitized_readings = filter_anomalies(raw_sensor_cluster)
final_diagnostic = analyze_readings(sanitized_readings)

# Misleading secondary calculations
shadow_diagnostic = analyze_readings([-x for x in sanitized_readings])
consistency_score = abs(final_diagnostic - shadow_diagnostic) // 100 if shadow_diagnostic != -999 else 0
validation_cycle = [x * 0.99 for x in raw_sensor_cluster if x > 0.5]

# Output (only this matters)
print(f"Result: {final_diagnostic}")