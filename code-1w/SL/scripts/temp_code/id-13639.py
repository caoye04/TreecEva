import math

def sensor_calibration(raw_value, offset=0.73):
    return raw_value * 0.98 + offset

def evaluate_stability(risk_factor):
    return risk_factor > 5.2 and risk_factor < 9.1

def compute_entropy(data_stream):
    entropy = 0
    for x in data_stream:
        if x > 0:
            entropy -= x * math.log(x)
    return round(entropy, 4)

def extract_signals(raw_logs):
    signals = []
    for log in raw_logs:
        if 'error' not in log and 'timeout' not in log:
            signals.append(log['value'] if 'value' in log else 0)
    return signals

def filter_anomalies(signal_list):
    baseline = sum(signal_list) / len(signal_list)
    return [s for s in signal_list if abs(s - baseline) < 1.5]

def aggregate_diagnostics(flags):
    return sum([1 for f in flags if f]) % 7

def generate_synthetic_data(n):
    return [((i * 1.7) % 1.3) for i in range(n)]

def analyze_readings(metrics):
    temp_history = [m['temp'] for m in metrics if 'temp' in m]
    pressure_series = list(filter(lambda x: x > 0.5, [m.get('pressure', 0) for m in metrics]))
    
    # Irrelevant transformation (distractor)
    shadow_buffer = [math.sin(p) for p in pressure_series if p < 2.0]
    normalization_factor = compute_entropy(shadow_buffer) if shadow_buffer else 0.0
    
    # Misleading intermediate (dead path)
    diagnostic_flag = False
    if normalization_factor > 1.0:
        diagnostic_flag = True
        buffer_cache = [normalization_factor * 2]  # Unused
    
    # Real computation begins
    valid_temps = list(filter_anomalies(temp_history))
    adjusted_temps = [sensor_calibration(t, 0.15) for t in valid_temps]
    
    # Decoy function call with no effect
    _ = generate_synthetic_data(len(adjusted_temps))
    
    avg_temp = sum(adjusted_temps) / len(adjusted_temps) if adjusted_temps else 0
    stability_score = avg_temp * 0.87
    
    # Complex conditional red herring
    if evaluate_stability(stability_score):
        fallback_array = [stability_score * 2 for _ in range(5)]
        mid_correction = sum(fallback_array) / 10
        stability_score = mid_correction  # Overwritten but not used later
    
    # Core logic embedded in distractions
    critical_threshold = 6.54
    adjustment_curve = [math.pow(t, 0.92) for t in adjusted_temps]
    
    # Final calculation
    base_metric = sum(adjustment_curve) / len(adjustment_curve) if adjustment_curve else 0
    final_score = base_metric * 1.15
    
    # Key result
    final_diagnostic = int(round(final_score * 100))
    return final_diagnostic

# Simulated input data (real signal)
data_logs = [
    {'value': 1.2, 'type': 'normal'},
    {'value': 0.9, 'type': 'normal'},
    {'error': 'crc', 'type': 'skip'}
]

# Generate primary metrics
raw_metrics = [
    {'temp': 5.8, 'pressure': 1.2},
    {'temp': 6.1, 'pressure': 0.9},
    {'temp': 5.9, 'pressure': 1.8},
    {'temp': 6.3, 'pressure': 0.4},
    {'temp': 6.0, 'pressure': 2.1}
]

processed_signals = extract_signals(data_logs)
signal_dump = {'raw': processed_signals, 'count': len(processed_signals)}

# Apply filtering (distraction)
cleaned_signals = [s * 1.1 for s in processed_signals if s > 0.5]

# Main metric processing
processed_metrics = [
    {'temp': m['temp'] * 1.03, 'pressure': m['pressure']} 
    for m in raw_metrics
]

# Add decoy computations
baseline_offset = 0.05
offset_buffer = [baseline_offset * i for i in range(10)]
dummy_flags = [True, False, True]
useless_diagnostic = aggregate_diagnostics(dummy_flags)

# Critical execution point
final_diagnostic = analyze_readings(processed_metrics)

# Output result
print(f"Result: {final_diagnostic}")