from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic analysis

def collect_raw_readings():
    # Real data source (simplified)
    return [
        (101, [23.4, 24.1, 22.8, 25.0, 23.9]),
        (102, [19.5, 18.7, 19.0, 18.2, 19.8]),
        (103, [31.2, 32.0, 30.8, 33.1, 31.7]),
        (104, [17.6, 16.9, 18.1, 17.3, 17.9])
    ]

def filter_outliers(values, factor=1.5):
    """Remove outliers using IQR method"""
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [v for v in values if lower <= v <= upper]

def rolling_average(values, window=3):
    if len(values) < window:
        return values
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages

def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    probabilities = [count / total for count in counts.values()]
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

def apply_calibration(readings_map, calib_factor=0.98):
    # Irrelevant calibration for alternate system
    calibrated = {}
    for key, vals in readings_map.items():
        calibrated[key] = [v * calib_factor for v in vals]
    return calibrated  # Unused in final logic

def generate_synthetic_data(n):
    # Dead code path — generates fake data not used in main flow
    synthetic = {}
    for i in range(n):
        synthetic[i] = [math.sin(i + j) * 20 for j in range(5)]
    return synthetic

def detect_spikes(values, spike_threshold=1.8):
    # Misleading auxiliary function that isn't used in final analysis
    spikes = 0
    for i in range(1, len(values)):
        if abs(values[i] - values[i-1]) > spike_threshold:
            spikes += 1
    return spikes

def normalize_readings(values):
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.5 for _ in values]
    return [(v - min_val) / (max_val - min_val) for v in values]

def classify_regime(avg_temp):
    if avg_temp < 20:
        return 'cold'
    elif avg_temp < 30:
        return 'moderate'
    else:
        return 'hot'

def build_threshold_map(regimes):
    base_map = defaultdict(lambda: 0.5)
    for rid, regime in regimes.items():
        if regime == 'cold':
            base_map[rid] = 0.65
        elif regime == 'moderate':
            base_map[rid] = 0.75
        else:
            base_map[rid] = 0.85
    # Add decoy entries
    base_map['calibration_offset'] = 0.02
    base_map['debug_flag'] = 1
    return base_map

def process_temperature_data(raw_entries):
    processed = {}
    entropy_log = []
    
    for sensor_id, readings in raw_entries:
        filtered = filter_outliers(readings)
        normalized = normalize_readings(filtered)
        rolled = rolling_average(normalized, 2)  # Smoothing
        avg_normalized = sum(rolled) / len(rolled) if rolled else 0
        
        # Compute entropy as a complexity measure (used later)
        quantized = [round(x * 10) for x in normalized]
        entropy = compute_entropy(quantized)
        entropy_log.append((sensor_id, entropy))
        
        # Store processed signal
        processed[sensor_id] = {
            'cleaned': filtered,
            'norm_avg': avg_normalized,
            'entropy': entropy,
            'stability': 1 - entropy  # Inverse relationship
        }
    
    # Secondary processing: derive global patterns (distraction)
    global_entropy = sum(e for _, e in entropy_log) / len(entropy_log) if entropy_log else 0
    system_wide_flag = global_entropy > 0.7
    
    # Unused intermediate structure
    summary_snapshot = {
        'timestamp': '2023-11-05T10:00:00Z',
        'sensor_count': len(processed),
        'high_entropy': system_wide_flag,
        'aux_data': [math.tanh(e) for _, e in entropy_log]
    }
    
    return processed

def analyze_readings(proc_data, thresholds):
    diagnostics = []
    debug_weights = []
    
    # Simulate multi-factor diagnostic scoring
    for sid, data in proc_data.items():
        base_score = data['norm_avg'] * 100
        entropy_penalty = data['entropy'] * 20
        threshold = thresholds[sid]
        
        # Weighted combination
        adjusted = base_score - entropy_penalty
        weight = 0.4 + (threshold * 0.6)  # Boost by threshold sensitivity
        contribution = adjusted * weight
        debug_weights.append((sid, weight, contribution))
        
        # Apply non-linear boost if stable
        if data['stability'] > 0.7:
            contribution = contribution * 1.15
        
        diagnostics.append(contribution)
    
    # Final aggregation
    raw_total = sum(diagnostics)
    adjustment_factor = 0.92
    
    # Decoy calculation - looks important but unused
    outlier_contributions = [d for d in diagnostics if d > 30]
    if len(outlier_contributions) > 1:
        adjustment_factor *= 0.98
    
    # Actual final result
    final_sum = raw_total * adjustment_factor
    
    # Additional red herring: transform into 'diagnostic code'
    code_points = [int(abs(final_sum) % 26) + ord('A')]
    diagnostic_letter = chr(code_points[0])
    
    # But we actually just need the numeric diagnostic score
    return int(round(final_sum))

# --- Main Execution ---
if __name__ == '__main__':
    # Step 1: Collect real sensor readings
    raw_sensor_data = collect_raw_readings()
    
    # Step 2: Process data through pipeline
    processed_data = process_temperature_data(raw_sensor_data)
    
    # Step 3: Classify each sensor's thermal regime for adaptive thresholds
    regimes = {}
    for sid, pdata in processed_data.items():
        avg_celsius = (pdata['norm_avg'] * 10) + 15  # Reverse normalize approx
        regimes[sid] = classify_regime(avg_celsius)
    
    # Step 4: Build dynamic threshold map based on regime
    threshold_map = build_threshold_map(regimes)
    
    # Step 5: Perform final diagnostic analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Irrelevant post-analysis (distractor)
    recalibrate_system = False
    if final_diagnostic > 120:
        recalibrate_system = True
    
    log_entry = f"DIAG-{final_diagnostic:X}-FLAG{int(recalibrate_system)}"
    
    # Output target result
    print(f"Target result: {final_diagnostic}")