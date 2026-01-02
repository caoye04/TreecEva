from collections import defaultdict, Counter
import math

# Simulated sensor data feed (realistic domain: health monitoring system)
def generate_telemetry():
    return {
        'heart_rate': [72, 75, 78, 80, 69, 74, 77],
        'oxygen': [98.2, 97.5, 96.8, 98.1, 97.9, 98.3, 97.2],
        'temperature': [36.6, 36.8, 37.1, 37.3, 36.9, 37.0, 37.2],
        'activity': [200, 450, 600, 300, 500, 550, 400]
    }

def analyze_rhythm(peaks):
    # Irrelevant red herring function - mimics signal processing but unused
    if len(peaks) < 2:
        return 0.0
    intervals = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    variance = sum((x - sum(intervals)/len(intervals))**2 for x in intervals) / len(intervals)
    return round(math.sqrt(variance), 3)

def compute_rolling_average(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return [round(x, 2) for x in smoothed]

def detect_spikes(values, threshold_multiplier=1.8):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val)**2 for x in values) / len(values)) ** 0.5
    spike_limit = mean_val + threshold_multiplier * std_dev
    return [i for i, v in enumerate(values) if v > spike_limit]

def evaluate_stability(metric_log):
    # Distractor: complex logic that isn't actually used in final path
    if len(metric_log) < 5:
        return 'UNSTABLE'
    diffs = [abs(metric_log[i] - metric_log[i-1]) for i in range(1, len(metric_log))]
    trend = sum(1 if d > 0 else -1 for d in diffs)
    if abs(trend) > len(diffs) * 0.6:
        return 'DETERIORATING' if trend > 0 else 'IMPROVING'
    return 'STABLE'

def aggregate_risk_scores(readings):
    # Dead code path - never called, but looks important
    scores = defaultdict(int)
    for key, values in readings.items():
        baseline = sum(values[:3]) / 3
        current = sum(values[-3:]) / 3
        change = (current - baseline) / baseline
        scores[key] = int(abs(change) * 100)
    return dict(scores)

def calculate_entropy(data):
    # Misleading intermediate calculation with bit manipulation red herring
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    # Bit twiddling distraction
    magic = 0
    for i in range(8):
        magic ^= (int(entropy * 1000) >> i) & 1
    return round(entropy + magic * 0.01, 4)

def validate_coherence(dataset):
    # Unused validation function with nested complexity
    flags = []
    for modality, series in dataset.items():
        zipped = list(zip(series[1:], series[:-1]))
        monotonic_up = all(a >= b for a, b in zipped)
        flags.append((modality, monotonic_up))
    return dict(flags)

def process_metrics(data, config):
    # Core logic buried among distractions
    hr_series = data['heart_rate']
    o2_series = data['oxygen']
    temp_series = data['temperature']
    
    # Real computation begins here
    avg_hr = sum(hr_series) / len(hr_series)
    o2_avg = sum(o2_series) / len(o2_series)
    temp_trend = temp_series[-1] - temp_series[0]
    
    # Key transformation: normalize and combine
    normalized_hr = (avg_hr - 70) * 1.5
    normalized_o2 = (98 - o2_avg) * 2.0  # inverted: lower O2 = higher risk
    
    # Weighted diagnostic score
    raw_score = (normalized_hr * 0.6) + (normalized_o2 * 0.3) + (temp_trend * 0.1)
    
    # Additional correction based on activity level pattern (distractor-heavy section)
    activity = data['activity']
    act_avg = sum(activity) / len(activity)
    peak_activity = max(activity)
    # Following lines look important but only act_avg is used
    _, *middle, _ = activity  # unpacking distraction
    median_like = sorted(middle)[len(middle)//2]
    activity_ratio = peak_activity / (act_avg + 1e-8)
    
    # Only this line matters from above
    adjustment_factor = 1.0 if act_avg < 500 else 1.15
    
    # Final computation
    diagnostic_value = raw_score * adjustment_factor
    
    # Redundant rounding and type conversion
    final_diagnostic = int(round(diagnostic_value * 100)) / 100.0
    
    # Decoy output variables
    summary_stats = {
        'entropy': calculate_entropy(hr_series),
        'spike_count': len(detect_spikes(temp_series)),
        'rhythm_consistency': analyze_rhythm(list(range(len(hr_series))))
    }
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Initialize system parameters (many irrelevant ones)
    thresholds = {
        'hr_max': 100,
        'o2_min': 95,
        'temp_critical': 38.0,
        'activity_threshold': 450
    }
    
    # Generate realistic health data
    health_data = generate_telemetry()
    
    # Perform comprehensive analysis
    preliminary_checks = validate_coherence(health_data)
    risk_profile = aggregate_risk_scores(health_data)  # dead call
    stability_status = evaluate_stability(health_data['temperature'])
    
    # Actual critical computation
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")