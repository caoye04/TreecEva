import itertools

# Simulated system telemetry data with mixed signal types
def generate_signals():
    base_frequency = 7
    harmonics = [base_frequency * i for i in range(1, 6)]
    phase_shifts = [0.5, 1.2, -0.3, 0.8, 1.5]
    signals = []
    for h, p in zip(harmonics, phase_shifts):
        wave = [(h * t + p) % (2 * 3.14159) for t in [0.1, 0.2, 0.3]]
        signals.append(wave)
    return signals

# Irrelevant auxiliary function - dead code path
def analyze_spectrum(data):
    magnitude = sum([sum(seq) for seq in data]) / len(data)
    spectral_index = magnitude * 1.732
    return spectral_index

# Core processing pipeline
def extract_features(signals):
    features = []
    for seq in signals:
        # Apply windowing (dummy operation)
        windowed = [x * 0.5 for x in seq]
        # Compute basic stats
        avg = sum(windowed) / len(windowed)
        peak = max(windowed)
        ratio_metric = peak / (avg + 1e-8)
        features.append((avg, peak, ratio_metric))
    return features

# Decoy transformation chain
def transform_legacy(features):
    transformed = []
    for f in features:
        x, y, z = f
        temp_a = x * 1.1 + 0.5
        temp_b = y * 0.9 - 0.3
        # This result is never used
        dummy_result = (temp_a ** 2 + temp_b ** 2) ** 0.5
        transformed.append((temp_a, temp_b))
    return transformed

# Real metric computation with distractors embedded
def compute_diagnostics(features):
    diagnostics = []n    anomaly_score = 0
    stability_flag = True
    
    for i, (avg, peak, ratio) in enumerate(features):
        # Red herring: complex but unused calculation
        fourier_proxy = (i + 1) * avg * 3.14159 / 180
        harmonic_weight = (i % 2 + 1) * 0.5
        
        # Actual logic path
        if ratio > 2.5:
            anomaly_score += 1
        if avg < 0:
            stability_flag = False
        
        # Distractor: intermediate value that looks important
        entropy_proxy = -sum([p * (p + 1e-8) for p in [0.1, 0.2, 0.7]])
        
    # Key derived values
    normalized_anomaly = anomaly_score * 100
    security_lock = 1 if stability_flag else 0
    
    # Final diagnostic assembly
    final_value = normalized_anomaly + security_lock * 17
    diagnostics.append(final_value)
    
    # Additional decoy list - unused
    audit_trail = [f"CHK-{i}: PASSED" for i in range(len(features))]
    return diagnostics

# Legacy compatibility wrapper - misleading
def legacy_process(chain):
    return [x * 0.95 for x in chain]

# Main orchestration with multiple layers
log_entries = generate_signals()
feature_set = extract_features(log_entries)
legacy_chain = transform_legacy(feature_set)  # Unused result
raw_diagnostics = compute_diagnostics(feature_set)

# System threshold with distracting initialization
system_threshold = 120
config_override = False
if config_override:
    system_threshold *= 0.8  # Dead code path

intermediate_audit = list(itertools.chain.from_iterable([
    [f"DIAG-{i}" for i in range(3)]
]))  # Meaningless string list

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_threshold)

# Wrapper function that appears necessary but is actually simple
def process_metrics(entries, threshold):
    features = extract_features(entries)
    diag = compute_diagnostics(features)
    base_value = diag[0]
    
    # Apply threshold masking - always true in this case
    mask = 1 if base_value > threshold else 0
    adjustment = (threshold // 10) * mask
    
    # Final computation
    result = base_value + adjustment - 5
    
    # Print required output
    print(f"Result: {result}")
    return result

# Execute and print
final_diagnostic = process_metrics(log_entries, system_threshold)