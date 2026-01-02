import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_signal(raw_samples):
    filtered = []
    noise_floor = 0.041
    gain_compensation = 1.87
    for x in raw_samples:
        if abs(x) > noise_floor:
            filtered.append(x * gain_compensation)
    return filtered

# Irrelevant helper - dead code path (distractor)
def smooth_data(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed  # never used

# Red herring function: looks important but unused
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core transformation: applies phase shift and folds signal
def fold_signal(phases):
    folded = []
    for p in phases:
        shifted = (p + math.pi / 4) % (2 * math.pi)
        if shifted > math.pi:
            folded.append(2 * math.pi - shifted)
        else:
            folded.append(shifted)
    return [round(f, 6) for f in folded]

# Calibration logic with conditional expression
def apply_calibration(val, calib_map):
    base = calib_map.get('base_offset', 0.0)
    factor = calib_map.get('scale', 1.0) if val > 0.5 else calib_map.get('scale_neg', 0.8)
    return (val - base) * factor

# Main analysis function with dictionary operations and nested logic
def analyze_signal(buffer, calib):
    temp_results = {}
    
    # Step 1: Frequency extraction (irrelevant intermediate)
    peak_freq = 0
    for i in range(1, len(buffer) - 1):
        if buffer[i] > buffer[i-1] and buffer[i] > buffer[i+1]:
            peak_freq += 1
    temp_results['peaks'] = peak_freq
    
    # Step 2: Phase calculation (actually used)
    magnitudes = [abs(x) for x in buffer]
    avg_mag = sum(magnitudes) / len(magnitudes)
    phases = [math.atan2(x, avg_mag + 0.1) for x in buffer]
    
    # Step 3: Signal folding
    folded_phases = fold_signal(phases)
    
    # Step 4: Apply calibration using conditional logic
    calibrated_values = []
    for v in folded_phases:
        cv = apply_calibration(v, calib)
        calibrated_values.append(cv)
    
    # Step 5: Weighted diagnostic score (key computation)
    weights = {'w1': 0.35, 'w2': 0.45, 'w3': 0.2}
    w1_contrib = sum(calibrated_values[:3]) * weights['w1']
    w2_contrib = sum(calibrated_values[3:6]) * weights['w2']
    w3_contrib = sum(calibrated_values[6:]) * weights['w3'] * (1 + calib.get('boost', 0))
    
    # Final diagnostic with decoy variables and red herrings
    initial_estimate = w1_contrib + w2_contrib
    adjustment_factor = math.sin(len(buffer) * 0.1)
    final_diagnostic = initial_estimate + w3_contrib + adjustment_factor
    
    # Decoy assignments (irrelevant)
    temp_results['debug_code'] = 9182
    temp_results['status'] = 'OK'
    temp_results['final_value'] = final_diagnostic  # misleading nesting
    
    return final_diagnostic

# Simulated input data
raw_input = [-0.15, 0.08, 0.21, -0.03, 0.34, 0.19, -0.22, 0.07, 0.14]
pattern_buffer = preprocess_signal(raw_input)

# Calibration metadata (dictionary with red herring keys)
calibration_data = {
    'base_offset': 0.05,
    'scale': 1.15,
    'scale_neg': 0.95,
    'boost': 0.12,
    'version': '2.1',
    'timestamp': 1718923401,
    'diagnostics_enabled': False
}

# Dead variable assignment - misleading intermediate
intermediate_snapshot = [round(x, 3) for x in pattern_buffer]

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, calibration_data)

# Output result as required
print(f"Result: {final_diagnostic}")