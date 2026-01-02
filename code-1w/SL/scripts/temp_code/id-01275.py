import math

def analyze_phase_shift(frequency, amplitude, phase):
    if frequency <= 0:
        return 0.0
    shift = amplitude * math.sin(phase + (2 * math.pi * frequency * 0.001))
    normalized = (shift + amplitude) / (2 * amplitude)
    return round(normalized * 100, 4)

def generate_calibration_points(base_freq, steps):
    points = []
    for i in range(1, steps + 1):
        adjusted_freq = base_freq * (1 + 0.05 * i)
        score = analyze_phase_shift(adjusted_freq, 1.5, i)
        points.append((i, adjusted_freq, score))
    return points

def compute_entropy(data_list):
    total = sum(x[2] for x in data_list)
    if total == 0:
        return 0.0
    entropy = 0.0
    for item in data_list:
        prob = item[2] / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 5)

def validate_timing_sequence(sequence):
    if len(sequence) < 3:
        return False
    deltas = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    avg_delta = sum(deltas) / len(deltas)
    variance = sum((d - avg_delta) ** 2 for d in deltas) / len(deltas)
    return variance < 0.1

def extract_critical_windows(log_data, window_size=3):
    windows = []
    for i in range(len(log_data) - window_size + 1):
        window = log_data[i:i+window_size]
        avg_val = sum(window) / window_size
        windows.append((i, window, avg_val))
    return windows

def filter_anomalies(dataset, threshold=75.0):
    # Irrelevant filtering for distraction
    clean_set = [x for x in dataset if x[2] > threshold]
    return clean_set

def accumulate_diagnostics(raw_logs):
    cumulative = 0
    weights = [0.1, 0.2, 0.3, 0.4]
    for i, log in enumerate(raw_logs):
        weighted_val = log[2] * weights[i % 4]
        cumulative += weighted_val
    return round(cumulative, 3)

def aggregate_metrics(timing_log, calibration_sequence):
    # Real computation path
    entropy_metric = compute_entropy(calibration_sequence)
    
    # Distractor: irrelevant transformation
    shifted_log = [t * 1.001 for t in timing_log]
    valid_sequence = validate_timing_sequence(shifted_log)
    
    # Distractor: unused complex structure
    metadata_map = {
        'origin': 'sensor_hub_7',
        'version': '2.1.9-alpha',
        'checksum': sum(t**2 for t in timing_log[:5]) % 1000
    }
    
    # Real dependency
    critical_windows = extract_critical_windows(timing_log, 3)
    window_boost = sum(w[2] for w in critical_windows if w[2] > 400) * 0.01
    
    # Distractor: dead code path with decoy function
    def adjust_phase_integrity():
        return sum(math.cos(t) for t in timing_log)  # never called
    
    # Distractor: misleading intermediate
    temp_diagnostic = accumulate_diagnostics(calibration_sequence)
    baseline_score = temp_diagnostic * 0.67
    
    # Real contribution
    window_count_score = len([w for w in critical_windows if w[2] > 450])
    
    # Final calculation
    final_diagnostic = int(
        (entropy_metric * 50) + 
        window_boost + 
        (window_count_score * 15) + 
        (7 if valid_sequence else 0)
    )
    
    # Red herring: printing unrelated derived value
    debug_aux = (metadata_map['checksum'] + baseline_score) % 100
    print(f"Auxiliary debug metric: {debug_aux}")
    
    return final_diagnostic

# Simulated input data
timing_log = [120, 125, 130, 455, 460, 465, 140, 142, 144]
calibration_sequence = generate_calibration_points(50.0, 6)

# Key statement
final_diagnostic = aggregate_metrics(timing_log, calibration_sequence)
print(f"Target result: {final_diagnostic}")