import math

# Simulated biomedical signal processing system
def analyze_waveform(signal_data):
    if not signal_data:
        return 0
    
    # Irrelevant frequency harmonics (distraction)
    harmonic_series = [math.sin(x * 0.1) for x in range(10)]
    fft_peaks = sum([int(abs(h) > 0.5) for h in harmonic_series])

    # Core energy calculation
    total_energy = sum([x ** 2 for x in signal_data])
    avg_power = total_energy / len(signal_data)

    # Red herring: unused transformation
    normalized = [x / (max(signal_data) + 1e-9) for x in signal_data]
    envelope = max(normalized) - min(normalized)

    return avg_power

# Auxiliary function with misleading intermediate outputs
def compute_stress_index(values):
    base = sum(values) / len(values)
    variance = sum([(v - base) ** 2 for v in values]) / len(values)
    stress_factor = math.sqrt(variance) / (base + 1e-9)

    # Dead code path (never executed due to fixed condition)
    if False:
        correction = 0
        for v in values:
            if v > 3 * base:
                correction += 1
        stress_factor *= (1 + correction)

    # Distractor statistics
    peak_count = len([v for v in values if v > base * 1.5])
    decay_rate = (values[-1] - values[0]) / len(values) if len(values) > 1 else 0

    return stress_factor * 100

# Main diagnostic processor
def generate_health_signature(raw_readings):
    readings_log = [math.log(r + 1) for r in raw_readings]
    filtered = [r for r in readings_log if r > 0.5]
    
    # Complex but irrelevant clustering attempt
    clusters = {}
    for i, val in enumerate(filtered):
        key = int(val // 1)
        if key not in clusters:
            clusters[key] = []
        clusters[key].append(val)
    
    # Real metric: entropy approximation
    entropy = 0
    for val in filtered:
        prob = val / (sum(filtered) + 1e-9)
        if prob > 0:
            entropy -= prob * math.log(prob)
    
    # Dummy feature engineering
    trend_score = sum([filtered[i+1] - filtered[i] for i in range(len(filtered)-1)])
    volatility = compute_stress_index(filtered)

    # Actual signal used downstream
    return {'entropy': entropy, 'size': len(filtered), 'raw_len': len(raw_readings)}

# Threshold engine with red herrings
def evaluate_anomaly_profile(signature, config):
    # Multiple distractor thresholds
    thresholds = {
        'noise_floor': config.get('floor', 0.1),
        'saturation_limit': 100,
        'decay_guard': -5,
        'entropy_threshold': 2.1,
        'size_requirement': 6,
        'legacy_flag': True
    }
    
    # Unused conditional logic tree
    if signature['raw_len'] > 20:
        thresholds['entropy_threshold'] *= 1.1
    elif signature['raw_len'] < 5:
        thresholds['size_requirement'] = 3

    # Evaluate real conditions
    entropy_ok = signature['entropy'] > thresholds['entropy_threshold']
    size_ok = signature['size'] >= thresholds['size_requirement']
    
    # Composite score (partially irrelevant)
    score_components = [
        signature['entropy'] * 0.7,
        signature['size'] * 0.3
    ]
    composite = sum(score_components)
    
    # Final decision uses only two boolean conditions
    return {'passed': entropy_ok and size_ok, 'score': composite}

# Primary processing pipeline
def process_metrics(signature, threshold_map):
    # Multi-stage validation with distractions
    diagnostics = []
    
    # Stage 1: entropy check
    if 'entropy' in signature:
        norm_entropy = signature['entropy'] / (threshold_map['entropy_threshold'] + 1e-9)
        diagnostics.append(('entropy_norm', norm_entropy))
        
        # Conditional expression (required language feature)
        status = 'high' if norm_entropy > 1.2 else 'low'
        diagnostics.append(('entropy_status', status))
    
    # Stage 2: size validation
    min_size = threshold_map.get('size_requirement', 5)
    size_ratio = signature['size'] / min_size
    
    # Dictionary operation (required language feature)
    result_map = {
        'input_size': signature['size'],
        'required': min_size,
        'ratio': size_ratio
    }
    diagnostics.append(('size_analysis', result_map))
    
    # Stage 3: final integration
    passed_tests = 0
    for item in diagnostics:
        key = item[0]
        value = item[1]
        if key == 'entropy_norm' and value > 1.0:
            passed_tests += 1
        elif key == 'size_analysis' and isinstance(value, dict):
            if value['ratio'] >= 1.0:
                passed_tests += 1
    
    # Critical computation path
    base_score = signature['entropy'] * signature['size']
    adjustment = 1.0
    
    # Nested conditional with multiple levels (4-level nesting)
    if 'entropy' in signature:
        if signature['entropy'] > 0:
            inv_threshold = 1 / threshold_map['entropy_threshold']
            if inv_threshold > 0.4:
                if base_score > 10:
                    adjustment = 1.25
    
    adjusted_score = base_score * adjustment
    
    # Final diagnostic value (target variable)
    final_diagnostic = int(adjusted_score + passed_tests * 10)
    
    # Dead computation: buffer overflow mimicry (irrelevant)
    buffer_state = ['\x00'] * 16
    overflow_marker = False
    for i in range(len(buffer_state)):
        if i == signature.get('raw_len', 0) % 17:
            overflow_marker = True
    
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    # Input data
    sensor_stream = [2.1, 3.5, 4.8, 1.9, 6.2, 5.0, 3.7, 4.4, 2.8]
    
    # Irrelevant preprocessing chain
    scaled_data = [x * 1.05 for x in sensor_stream]
    clipped = [min(x, 5.0) for x in scaled_data]
    enhanced = [x + 0.1 for x in clipped]
    
    # Core processing begins here
    health_signature = generate_health_signature(enhanced)
    
    # Misleading threshold variants
    debug_thresholds = {'debug_mode': True, 'version': '2.1'}
    legacy_config = {'legacy_flag': True, 'deprecated': 1}
    
    # Actual threshold map used
    threshold_map = {
        'entropy_threshold': 1.8,
        'size_requirement': 7,
        'placeholder': None
    }
    
    # Trigger main analysis
    final_diagnostic = process_metrics(health_signature, threshold_map)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")