import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw = [i * 0.5 + (i % 7) for i in range(20)]
    offset = 12.8
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant auxiliary function (decoy)
def compute_health_score(metrics):
    score = 0
    for m in metrics:
        if m > 10:
            score += m * 0.3
        else:
            score += m * 0.1
    return int(score) % 100

# Signal conditioning with red herring operations
def filter_noise(data):
    filtered = []
    noise_floor = 5.2
    suppression_factor = 0.88
    temp_result = 0
    
    for val in data:
        if abs(val) > noise_floor:
            temp_result += val * suppression_factor
            filtered.append(val * suppression_factor)
        else:
            filtered.append(val)
    
    # Dead code path - never executed due to logic above
    if len(filtered) < 5:
        fallback = [0] * 5
        return fallback
        
    return filtered

# Data transformation with bitwise obfuscation layer
def encode_timestamp(values, base_time=16384):
    encoded = []
    mask = 0b111100001111
    shift = 3
    
    for i, v in enumerate(values):
        time_variant = base_time + i
        mixed = (int(v * 10) ^ time_variant) & mask
        shifted = (mixed << shift) | (mixed >> (16 - shift))
        encoded.append(shifted)
    
    # Distractor computation (unused)
    avg_encoded = sum(encoded) / len(encoded) if encoded else 0
    outlier_count = sum(1 for e in encoded if e > 5000)
    
    return encoded

# Core analysis with lambda-based reduction
def analyze_signal(encoded_data):
    # Lambda for dynamic thresholding (actual relevant logic)
    threshold_fn = lambda x: math.sin(x * 0.001) > 0.5
    
    candidates = []
    for val in encoded_data:
        if threshold_fn(val):
            candidates.append(val % 1000)
    
    # Real result computation
    aggregate = 0
    for c in candidates:
        if c % 3 == 0:
            aggregate += c // 3
        elif c % 2 == 0:
            aggregate += c // 2
        else:
            aggregate += c

    # Multiple irrelevant intermediate variables
    compression_ratio = len(candidates) / len(encoded_data) if encoded_data else 0
    entropy_proxy = math.log(aggregate) if aggregate > 0 else 0
    normalization_constant = 1.847
    dummy_correction = entropy_proxy * normalization_constant
    
    final_diagnostic = aggregate + 42
    return final_diagnostic

# Unused diagnostic chain (red herring)
def generate_report(snapshot):
    summary = {}
    summary['peak'] = max(snapshot) if snapshot else 0
    summary['baseline'] = snapshot[0] if snapshot else 0
    summary['variance'] = sum((x - summary['baseline'])**2 for x in snapshot)
    return summary

# Main execution flow
if __name__ == "__main__":
    samples = collect_samples()
    cleaned = filter_noise(samples)
    processed_data = encode_timestamp(cleaned)
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_data)
    
    # Irrelevant health assessment
    health_metrics = [len(processed_data), final_diagnostic, sum(processed_data)]
    score = compute_health_score(health_metrics)
    
    # Unused report generation
    report_snapshot = [final_diagnostic, score]
    report = generate_report(report_snapshot)
    
    print(f"Result: {final_diagnostic}")