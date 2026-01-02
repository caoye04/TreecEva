import math

def analyze_signal(samples, window_size=8):
    smoothed = []
    for i in range(len(samples)):
        start = max(0, i - window_size + 1)
        segment = samples[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(avg)
    return [round(x, 3) for x in smoothed]

def detect_peaks(values, sensitivity=0.5):
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            if values[i] > sensitivity * max(values):
                peaks.append(i)
    return peaks if peaks else [0]

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def generate_checksum(sequence):
    # Irrelevant red herring function - not used in final result
    chk = 0
    for val in sequence:
        chk = (chk << 1) ^ int(val * 100) & 0xFFFF
    return chk

def transform_coordinates(x_vals, y_vals):
    # Unused transformation - dead code path
    coords = list(zip(x_vals, y_vals))
    rotated = [(x*0.707 - y*0.707, x*0.707 + y*0.707) for x, y in coords]
    return rotated

def filter_outliers(data, factor=1.5):
    # Misleading intermediate processing
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    low = q1 - factor * iqr
    high = q3 + factor * iqr
    filtered = [x for x in data if low <= x <= high]
    return filtered or data[:len(data)//2]

def evaluate_stability(readings):
    diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    trend = sum(1 for d in diffs if d < 0.1) / len(diffs)
    return trend > 0.6

def aggregate_metrics(logs, config):
    baseline = config['base']
    tolerance = config['tolerance']
    
    # Core relevant logic
    adjusted = [x - baseline for x in logs]
    squared_devs = [(x ** 2) for x in adjusted]
    mean_sq = sum(squared_devs) / len(squared_devs)
    rmse = math.sqrt(mean_sq)
    
    # Distractor: complex but unused calculation
    dummy_stats = {
        'max': max(adjusted),
        'min': min(adjusted),
        'range': max(adjusted) - min(adjusted),
        'median': sorted(adjusted)[len(adjusted)//2]
    }
    
    # Another red herring using lambda and enumerate
    anomaly_score = sum(map(lambda x: x[0] * (x[1] % 0.5) if x[1] > 0.3 else 0,
                            enumerate(squared_devs)))
    
    # Real computation path
    if rmse < tolerance:
        score = 95 + (tolerance - rmse) * 100
    else:
        score = 95 - (rmse - tolerance) * 50
    
    # Final adjustment based on auxiliary condition (hidden dependency)
    peak_indices = detect_peaks(logs, sensitivity=0.4)
    if len(peak_indices) > 3:
        score -= 10
    
    # Critical assignment
    final_diagnostic = int(round(score))
    
    # Dead code with dictionary operations
    report = {
        'version': '2.1',
        'metrics': {
            'rmse': rmse,
            'anomaly': anomaly_score,
            'peaks': len(peak_indices)
        },
        'status': 'stable' if evaluate_stability(logs) else 'unstable'
    }
    report['diagnostics'] = {'code': final_diagnostic}
    
    return final_diagnostic

# Simulated sensor data - realistic domain context (telemetry diagnostics)
timing_data = [0.48, 0.51, 0.49, 0.53, 0.50, 0.47, 0.52, 0.51, 0.48, 0.49, 0.50, 0.54, 0.46, 0.50, 0.52]

# Configuration map with meaningful parameters
thresholds = {
    'base': 0.50,
    'tolerance': 0.025
}

# Irrelevant preprocessing chain
normalized = [x / max(timing_data) for x in timing_data]
scaled_ints = [int(x * 1000) for x in normalized]
bit_analysis = [(x & (x >> 1), x ^ (x + 1)) for x in scaled_ints[-5:]]

# Unused data structures
aux_data = list(enumerate(zip(normalized, scaled_ints)))
dummy_dict = {i: val for i, val in enumerate(bit_analysis)}

# Key execution point
final_diagnostic = aggregate_metrics(timing_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")