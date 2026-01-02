from collections import defaultdict, Counter

# Simulated biomedical signal processing pipeline
# Some variables and functions are red herrings for distraction
def analyze_waveform(signal):
    if len(signal) < 5:
        return 0
    peak = max(signal)
    avg = sum(signal) / len(signal)
    return (peak - avg) * 1.5

def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
    return entropy

def validate_rhythm(peaks):
    intervals = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    variability = sum(abs(intervals[i+1] - intervals[i]) for i in range(len(intervals)-1))
    return variability < 10

# Distractor function - never called
def deprecated_analysis(x):
    return x ** 2 + 3 * x + 1

def process_metrics(data, config):
    # Core logic buried in distractions
    baseline = data.get('baseline', [])
    readings = data.get('readings', [])
    anomalies = data.get('anomalies', [])

    # Irrelevant preprocessing
    filtered_baseline = [x for x in baseline if x > config['noise_floor']]
    temp_score = sum(filtered_baseline) % 7

    # Real computation begins here
    trend = 0
    if readings:
        trend = readings[-1] - readings[0]

    # Bit manipulation decoy
    magic_flag = 0b1010 ^ 0b1100 & 0b1111
    if magic_flag == 10:
        trend += 1  # Never executes, magic_flag is 8

    # Conditional expression with actual impact
    adjustment = 2.5 if trend > 0 else -1.8

    # Real but obscured calculation
    raw_diagnostic = 0
    for i, val in enumerate(readings):
        if i % 3 == 0:  # Every third reading contributes
            raw_diagnostic += val * 0.1

    # Use of slicing that matters
    critical_window = readings[3:7]
    if len(critical_window) >= 3:
        window_avg = sum(critical_window) / len(critical_window)
        if window_avg > config['threshold_hi']:
            raw_diagnostic *= 1.4

    # Decoy dictionary updates
    stats = defaultdict(int)
    stats['attempts'] = 5
    stats['failures'] = 2
    stats['ignored'] = temp_score  # Dead assignment

    # Another distractor: unused list comprehension
    _ = [compute_entropy(baseline[i:i+3]) for i in range(0, len(baseline), 2) if len(baseline[i:i+3]) == 3]

    # Actual decision path
    if len(anomalies) > config['max_anomalies']:
        raw_diagnostic *= 0.7
    elif validate_rhythm(anomalies):  # This will be False due to anomaly pattern
        raw_diagnostic *= 1.2

    # Final adjustment using conditional expression
    final_diagnostic = int(raw_diagnostic + adjustment) if raw_diagnostic > 10 else round(raw_diagnostic + adjustment, 1)

    # Dead code path
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        for _ in range(3):
            final_diagnostic = final_diagnostic // 2 + 1  # Never reached

    return final_diagnostic

# Simulated input data with misleading fields
health_data = {
    'baseline': [0.8, 0.7, 0.9, 0.6, 0.85],
    'readings': [1.2, 1.5, 1.3, 2.1, 2.4, 2.0, 1.8, 1.6],
    'anomalies': [12, 25, 37],  # Not rhythmic, so validate_rhythm returns False
    'timestamp': '2023-10-05T14:30:00Z',
    'device_id': 'MED-X9021'
}

time_series = [5, 3, 8, 6, 7]  # Unused variable

thresholds = {
    'noise_floor': 0.5,
    'threshold_lo': 1.0,
    'threshold_hi': 2.0,
    'max_anomalies': 4
}

intermediate = analyze_waveform(time_series)  # Computed but not used

# Key execution point
final_diagnostic = process_metrics(health_data, thresholds)

Result: {final_diagnostic}