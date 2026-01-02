import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw_data = [i * 0.5 + math.sin(i) for i in range(20)]
    offset = 127
    scaled = [int(x * 10 + offset) for x in raw_data]
    return scaled

# Irrelevant transformation - red herring
def transform_legacy(data):
    return [d ^ 255 for d in data[:10]]

# Unused checksum function - dead code path
def calculate_checksum(arr):
    chk = 0
    for val in arr:
        chk = (chk << 1) ^ val
    return chk & 0xFFFF

# Decoy analysis with misleading intermediate output
def superficial_scan(seq):
    peaks = [s for s in seq if s > 130]
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    print(f'Debug: Found {len(peaks)} high-amplitude samples')
    return avg_peak

# Signal conditioning with actual relevance
def filter_noise(data, threshold=125):
    filtered = []
    for sample in data:
        if abs(sample - 127) > threshold * 0.1:
            filtered.append(sample)
    # Misleading but unused statistic
    outlier_ratio = len(filtered) / len(data) if data else 0
    return filtered

# Real processing step - computes energy dispersion
def compute_dispersion(signal):
    if not signal:
        return 0.0
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    return round(math.sqrt(variance), 6)

# Data enrichment - actually used later
def augment_features(raw):
    magnitude = sum(abs(r - 127) for r in raw)
    entropy = 0.0
    hist = {}
    for r in raw:
        hist[r] = hist.get(r, 0) + 1
    total = len(raw)
    for count in hist.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return {'magnitude': magnitude, 'entropy': round(entropy, 6), 'count': len(raw)}

# Conditional transformation - only some branches are relevant
def process_critical_path(features, dispersion):
    level = 'low'
    if dispersion > 5.0:
        level = 'high'
    elif dispersion > 2.0:
        level = 'medium'
    else:
        level = 'minimal'
    
    # Complex weighting - partially irrelevant
    weights = {'low': 1.0, 'medium': 2.5, 'high': 4.0}
    score = features['magnitude'] * weights[level]
    
    # Distractor: unused modulation index
    mod_index = features['entropy'] * (1 + features['count'] // 10)
    
    adjusted_score = score * (1 + 0.1 * features['entropy'])
    return adjusted_score

# Core analysis function - depends on multiple prior results
def analyze_signal(samples):
    # Step 1: noise filtering (actually matters)
    cleaned = filter_noise(samples)
    
    # Step 2: compute dispersion (used in final result)
    dispersion_metric = compute_dispersion(cleaned)
    
    # Step 3: extract features (used)
    feats = augment_features(samples)
    
    # Step 4: process through critical logic (used)
    outcome = process_critical_path(feats, dispersion_metric)
    
    # Dead branch - never executed due to fixed input size
    if len(samples) > 100:
        backup = superficial_scan(samples)
        outcome = (outcome + backup) / 2
    
    # Final computation - this determines the answer
    diagnostic_value = int(outcome // 10 * (dispersion_metric + feats['entropy']))
    return diagnostic_value

# === MAIN EXECUTION ===
if __name__ == '__main__':
    # Collect initial sensor readings
    raw_samples = collect_samples()
    
    # Apply legacy transform (result unused - distraction)
    legacy_output = transform_legacy(raw_samples)
    
    # Perform superficial scan (output printed but not used)
    _ = superficial_scan(raw_samples)
    
    # Process main signal path
    processed_samples = raw_samples  # Direct pass-through after collection
    
    # Compute checksum (never called - decoy)
    # cs = calculate_checksum(processed_samples)
    
    # Critical analysis chain
    final_diagnostic = analyze_signal(processed_samples)
    
    # Output target result
    print(f"Result: {final_diagnostic}")