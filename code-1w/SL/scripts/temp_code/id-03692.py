import math

# Simulated sensor fusion system for environmental monitoring

def collect_sensor_data():
    raw_data = [127, 255, 192, 64, 224, 32, 160, 96]
    offset = 128
    adjusted = [x - offset for x in raw_data]
    return adjusted

def filter_noise(signal):
    # Apply high-pass filter via bit manipulation (simulated)
    filtered = []
    for x in signal:
        if abs(x) > 32:
            # Bitwise transformation to simulate frequency filtering
            transformed = (x & 0b11111000) | (x >> 5)
            filtered.append(transformed)
        else:
            filtered.append(0)
    return filtered

def extract_features(data):
    # Extract statistical and spectral features
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    peak = max(abs(x) for x in data)
    
    # Irrelevant intermediate calculations (distractors)
    dummy_freq = 0
    for i in range(len(data)):
        dummy_freq += int(math.sin(math.pi * i / 4) * 10)
    
    # Real feature vector
    features = {
        'avg': round(mean_val, 3),
        'var': round(variance, 3),
        'peak': peak,
        'count_nonzero': len([x for x in data if x != 0])
    }
    return features

def transform_coordinates(features):
    # Simulate spatial mapping (irrelevant to final result but looks important)
    x = features['avg'] * 1.5
    y = features['var'] / 2.0
    z = features['peak'] * 0.1
    
    # Dummy transformation using lambda (red herring)
    project_2d = lambda a, b: (a + b) % 100
    projection = project_2d(x, y)
    
    # Return original features unchanged (decoy function)
    return features

def integrate_system_state(features):
    # Simulate integration with external system state (distraction)
    system_log = []
    for k, v in features.items():
        system_log.append(f"{k}:{v}")
    
    # Dead code path - never executed due to condition
    if len(system_log) < 5:
        system_log.append("redundant_backup")
    
    # Return same features (no actual change)
    return features

def compute_harmonic_index(features):
    # Compute harmonic distortion index from signal characteristics
    base = features['avg']
    variation = features['var']
    magnitude = features['peak']
    
    # Complex formula with irrelevant branches
    if magnitude > 50:
        index = (variation / (abs(base) + 1)) * magnitude
        if index > 100:
            index = index / 2  # correction factor
        # Additional decoy computation
        temp = 0
        for i in range(5):
            temp += int(math.log(max(i+1, 2)) * base)
    else:
        index = 0
    
    # Final index scaled logarithmically
    return math.log(index + 1) if index > 0 else 0

def generate_report(features):
    # Generate diagnostic report string (completely irrelevant)
    report_lines = []
    report_lines.append("=== SYSTEM DIAGNOSTIC ===")
    for key, val in features.items():
        report_lines.append(f"{key.upper()}: {val}")
    report_lines.append("STATUS: NOMINAL")
    return '\n'.join(report_lines)

def analyze_readings(signals):
    processed = []
    for s in signals:
        if s != 0:
            # Apply non-linear response curve
            processed.append(int(math.tanh(abs(s)/50) * s))
        else:
            processed.append(0)
    
    # Extract real features used in final calculation
    feats = extract_features(processed)
    
    # Chain of transformations (some irrelevant)
    feats = transform_coordinates(feats)          # No-op effectively
    feats = integrate_system_state(feats)         # No-op
    
    # Critical step: compute harmonic index
    harmonic_score = compute_harmonic_index(feats)
    
    # Generate report (unused)
    _ = generate_report(feats)
    
    # Final diagnostic combines multiple sources
    base_diagnostic = feats['avg'] * 10
    variance_factor = math.sqrt(feats['var'])
    harmonic_contribution = harmonic_score * 20
    
    # Final computation (depends on harmonic_score which depends on earlier logic)
    final_diagnostic = int(base_diagnostic + variance_factor + harmonic_contribution)
    
    # Red herring: unused alternative calculation
    alternative = 0
    if feats['count_nonzero'] > 4:
        alternative = int((feats['peak'] ** 1.5) / 10)
    
    return final_diagnostic

# Main execution flow
if __name__ == "__main__":
    # Collect raw sensor data
    raw_signals = collect_sensor_data()
    
    # Filter out noise components
    filtered_signals = filter_noise(raw_signals)
    
    # Process signals through pipeline
    processed_signals = [x * 2 for x in filtered_signals]  # Amplification stage
    
    # Introduce irrelevant list slicing operation (distractor)
    window_slice = processed_signals[2:6]
    slice_sum = sum(window_slice)
    normalization_factor = slice_sum / 100.0 if slice_sum != 0 else 1.0
    
    # Another decoy dictionary operation
    stats_summary = {
        'range': max(processed_signals) - min(processed_signals),
        'midpoint': (max(processed_signals) + min(processed_signals)) / 2,
        'norm_factor': normalization_factor
    }
    
    # Core analysis chain
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")