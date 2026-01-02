from collections import defaultdict, Counter
import math

# Simulated sensor array data with noise and redundant channels
temperature_reads = [23.5, 24.1, 23.9, 25.0, 26.2, 25.8, 24.3, 23.7]
humidity_reads = [45, 47, 50, 52, 48, 55, 60, 53]
pressure_reads = [1013, 1012, 1014, 1015, 1016, 1013, 1011, 1010]

# Irrelevant auxiliary data (distractor)
satellite_sync_log = ['OK', 'RETRY', 'OK', 'FAIL', 'OK', 'OK', 'N/A', 'OK']
packet_sequence = list(range(1000, 1008))

def normalize_readings(raw_data):
    mean_val = sum(raw_data) / len(raw_data)
    return [round(x - mean_val, 3) for x in raw_data]

def detect_outliers(data, threshold=1.5):
    normalized = normalize_readings(data)
    stdev = (sum(x**2 for x in normalized) / len(normalized)) ** 0.5
    return [i for i, x in enumerate(normalized) if abs(x) > threshold * stdev]

def compute_entropy(values):
    count_map = Counter(values)
    total = len(values)
    return round(-sum((freq/total) * math.log2(freq/total) for freq in count_map.values()), 4)

# Dead function - never called (red herring)
def legacy_calibrate(x):
    return (x * 0.987) + 2.1

# Signal filtering using moving average (partially relevant)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        segment = signal[start:i+1]
        smoothed.append(round(sum(segment) / len(segment), 3))
    return smoothed

# Complex diagnostic chain with nested logic
def analyze_sensor_fusion(temp, humid, press):
    temp_outliers = detect_outliers(temp)
    humid_entropy = compute_entropy([x // 5 * 5 for x in humid])  # bucketed
    press_trend = [press[i+1] - press[i] for i in range(len(press)-1)]
    
    # Distractor computation
    sync_consistency = sum(1 for x in satellite_sync_log if x in ['OK', 'RETRY'])
    
    # Core metric: weighted instability index
    outlier_penalty = len(temp_outliers) * 10
    entropy_bonus = int(humid_entropy * 20)
    trend_volatility = abs(sum(press_trend))
    
    base_score = 100 - outlier_penalty + entropy_bonus - trend_volatility
    
    # Simulated correction for false anomalies
    if len(temp_outliers) == 2 and press[0] < press[-1]:
        base_score += 15  # compensation heuristic
    
    return max(10, min(100, base_score))  # clamped

# Data transformation pipeline with red herrings
def build_processing_chain(raw_temp, raw_humid, raw_press):
    processed_temps = normalize_readings(raw_temp)
    filtered_humidity = [x for x in raw_humid if x > 40]  # conditional filter
    
    # Unused intermediate (distractor)
    pressure_zscores = [round((x - sum(raw_press)/len(raw_press)) / 3.5, 3) for x in raw_press]
    
    # Tuple-based packing (relevant)
    readings_snapshot = list(zip(processed_temps, filtered_humidity[:len(processed_temps)]))
    
    # List comprehension with side filtering
    significant_shifts = [
        (i, t, h) for i, (t, h) in enumerate(readings_snapshot)
        if abs(t) > 0.8 or h > 50
    ]
    
    return {
        'snapshots': readings_snapshot,
        'shifts': significant_shifts,
        'temp_range': (min(processed_temps), max(processed_temps)),
        'aux_data': packet_sequence.copy()  # irrelevant but passed along
    }

# Aggregate multiple diagnostics (key function)
def aggregate_metrics(chain, diagnostics):
    shift_count = len(chain['shifts'])
    temp_span = chain['temp_range'][1] - chain['temp_range'][0]
    raw_diagnostic_score = diagnostics
    
    # Multiple layers of weighting
    stability_factor = 1 + (shift_count * 0.1)
    span_impact = temp_span * 2.5
    
    # Misleading intermediate that looks important
    aux_correlation = sum(1 for x in chain['aux_data'] if x % 2 == 0)
    adjusted_aux = aux_correlation * 0.05  # negligible effect
    
    result = raw_diagnostic_score * stability_factor - span_impact
    result -= adjusted_aux  # almost no impact
    
    return int(round(result))

# Orchestration block
if __name__ == "__main__":
    # Initial diagnostics from fused analysis
    initial_diagnostic = analyze_sensor_fusion(temperature_reads, humidity_reads, pressure_reads)
    
    # Build processing chain (contains distractors)
    processing_chain = build_processing_chain(temperature_reads, humidity_reads, pressure_reads)
    
    # Simulated secondary metrics (unused but computed)
    humidity_mode = Counter(humidity_reads).most_common(1)[0][1]
    pressure_stddev = round((sum((x - sum(pressure_reads)/8)**2 for x in pressure_reads)/8)**0.5, 3)
    
    # Critical execution point
    final_diagnostic = aggregate_metrics(processing_chain, initial_diagnostic)
    
    print(f"Result: {final_diagnostic}")