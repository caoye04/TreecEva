import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis

def collect_readings():
    raw_signals = [0.8, 1.2, 3.1, 2.9, 5.0, 5.1, 4.8, 7.2, 6.9, 7.0]
    timestamps = list(range(10))
    statuses = ['OK', 'OK', 'ERR', 'OK', 'OK', 'OK', 'OK', 'WARN', 'OK', 'OK']
    return list(zip(timestamps, raw_signals, statuses))

def filter_anomalies(data):
    clean_data = []
    noise_floor = 0.5
    for t, val, status in data:
        if status == 'ERR':  # Critical failure, skip
            continue
        if val > noise_floor:  # Valid signal above noise
            clean_data.append((t, val))
    return clean_data

def generate_reference_pattern():
    # Irrelevant synthetic pattern for distraction
    return [pow(2, n) % 10 for n in range(10)]

def extract_peaks(signal_sequence):
    peaks = []
    for i in range(1, len(signal_sequence) - 1):
        if signal_sequence[i] > signal_sequence[i-1] and signal_sequence[i] > signal_sequence[i+1]:
            peaks.append(signal_sequence[i])
    return peaks

def rolling_average(values, window=2):
    # Unused helper — red herring
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def transform_signal(paired_data):
    times, values = zip(*paired_data)
    normalized = [v / max(values) for v in values]
    derivative = [normalized[i+1] - normalized[i] for i in range(len(normalized)-1)]
    smoothed = [sum(normalized[max(0,i-1):i+2]) / len(normalized[max(0,i-1):i+2]) for i in range(len(normalized))]
    return {
        'time': times,
        'norm': normalized,
        'deriv': derivative,
        'smooth': smoothed
    }

def analyze_pattern(processed, settings):
    segment = processed['norm'][1:-1]  # Exclude edges
    trend_score = sum(segment) * settings['sensitivity']
    fluctuation = sum(abs(x) for x in processed['deriv'])
    
    # Apply masking based on irrelevant reference (distractor)
    ref_mask = generate_reference_pattern()
    masked_trend = trend_score
    for i, m in enumerate(ref_mask[:5]):
        if m % 2 == 0:
            masked_trend *= 0.9  # Misleading adjustment path
    
    # Real logic branch
    if fluctuation > settings['threshold']:
        adjustment = settings['penalty']
    else:
        adjustment = settings['bonus']
    
    result = int((masked_trend + adjustment) * 1000)  # Final deterministic integer
    
    # Dead code path — never executed due to fixed input
    if False and any(x > 100 for x in ref_mask):
        result = -999999
    
    return result

# Irrelevant data structures for distraction
system_logs = [
    {'level': 'DEBUG', 'msg': 'Init complete'},
    {'level': 'INFO', 'msg': 'Idle'},
    {'level': 'WARN', 'msg': 'Cache low'}
]

config = {
    'sensitivity': 2.5,
    'threshold': 1.0,
    'penalty': -50,
    'bonus': 42,
    'debug_mode': False
}

# Unused function — decoy
def validate_checksum(data):
    return sum(hash(str(d)) % 100 for d in data) % 7 == 0

# Main execution flow
raw_input = collect_readings()
cleaned = filter_anomalies(raw_input)
transformed_data = transform_signal(cleaned)

# Key statement
final_diagnostic = analyze_pattern(transformed_data, config)

# Print target result
print(f"Target result: {final_diagnostic}")