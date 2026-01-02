import math

# Simulated health monitoring system with data processing and diagnostic logic
def analyze_heart_rate(data):
    average_hr = sum(data) / len(data)
    resting_estimate = min(data)
    max_hr = max(data)
    hr_ratio = average_hr / resting_estimate if resting_estimate else 0
    # Irrelevant transformation
    dummy_calc = (max_hr ** 0.5) * 1.618
    return {
        'avg': average_hr,
        'resting': resting_estimate,
        'ratio': hr_ratio,
        'noise': dummy_calc  # Distractor field
    }

def compute_oxygen_trend(o2_levels):
    trend = []
    for i in range(1, len(o2_levels)):
        trend.append(o2_levels[i] - o2_levels[i - 1])
    avg_trend = sum(trend) / len(trend) if trend else 0
    severity = 'stable' if abs(avg_trend) < 0.5 else 'fluctuating'
    # Decoy metric
    phantom_index = sum(x ** 2 for x in o2_levels) % 7
    return {'trend': avg_trend, 'status': severity, 'phantom': phantom_index}

def filter_anomalies(signal):
    # Simple moving average filter (irrelevant to final result)
    window = 3
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        segment = signal[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    # Return only length as red herring output
    return len(smoothed)

def aggregate_scores(metrics_list):
    # Unused aggregation function (dead code path)
    total = 0
    for m in metrics_list:
        if 'score' in m:
            total += m['score']
    return total

# Lambda functions used for dynamic thresholding (actual relevant logic)
adaptive_scale = lambda x: math.log(x + 1) if x > 0 else 0
threshold_fn = lambda datum: 0.75 if adaptive_scale(datum['oxygen']) > 1.1 else 0.6

# Simulated patient health data
health_data = [
    {'heart_rate': [72, 75, 70, 80, 78], 'oxygen': 96, 'temperature': 36.8},
    {'heart_rate': [68, 70, 65, 72, 71], 'oxygen': 94, 'temperature': 37.1},
    {'heart_rate': [85, 90, 95, 92, 88], 'oxygen': 92, 'temperature': 38.2},
    {'heart_rate': [70, 71, 69, 73, 70], 'oxygen': 97, 'temperature': 36.5}
]

# Irrelevant preprocessing steps
normal_temps = [d['temperature'] for d in health_data]
avg_temp = sum(normal_temps) / len(normal_temps)
temp_deviation = [abs(t - avg_temp) for t in normal_temps]
baseline_ref = math.exp(avg_temp / 10)  # Unused reference

# Signal data (unrelated to diagnostics)
eeg_signal = [0.5, 0.7, 1.2, 0.8, 0.6, 1.0, 1.1]
signal_size = filter_anomalies(eeg_signal)  # Dead-end computation

# Real-time oxygen history (partially used)
o2_history = [96, 95, 94, 93, 94, 92, 91, 90]
o2_analysis = compute_oxygen_trend(o2_history)

# Core processing pipeline
processed_records = []
for entry in health_data:
    hr_data = entry['heart_rate']
    hr_metrics = analyze_heart_rate(hr_data)
    scaled_o2 = adaptive_scale(entry['oxygen'])
    
    # Intermediate score with misleading name
    risk_indicator = hr_metrics['ratio'] * 10 - scaled_o2
    
    # Actual relevant features
    record = {
        'hr_avg': hr_metrics['avg'],
        'oxygen_level': entry['oxygen'],
        'scaled_o2': scaled_o2,
        'risk_shadow': risk_indicator,  # Looks important but not directly used
        'metabolic_factor': hr_metrics['avg'] / (entry['oxygen'] + 1)
    }
    processed_records.append(record)

# Decision logic involving lambda-based threshold
def process_metrics(records, thresh_func):
    scores = []
    for rec in records:
        # Only this computation feeds into final result
        if thresh_func(rec) > 0.7:
            scores.append(rec['metabolic_factor'] * 100)
        else:
            scores.append(rec['metabolic_factor'] * 85)
    
    # Red herring: complex weighting that isn't used
    weights = [1.0 + math.sin(i) for i in range(len(scores))]
    weighted_total = sum(w * s for w, s in zip(weights, scores))
    
    # Final diagnostic is simple sum (non-obvious due to distractions)
    final_diagnostic = int(sum(scores))
    
    # More decoy operations
    entropy = -sum(math.log(abs(s) + 1e-5) for s in scores)
    calibration_offset = len(weights) * 0.15
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_fn)

# Output result as required
print(f"Target result: {final_diagnostic}")