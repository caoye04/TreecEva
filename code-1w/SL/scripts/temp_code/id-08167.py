import math

# Simulated biomedical signal processing pipeline with diagnostic analysis

def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return [round(x, 6) for x in normalized]


def compute_entropy(values):
    counts = {}
    for v in values:
        bucket = int(v * 10)
        counts[bucket] = counts.get(bucket, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 6)


def detect_spike_pattern(seq):
    spikes = 0
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1] and seq[i] > 0.8:
            spikes += 1
    return spikes > 2


def evaluate_stability_index(readings):
    diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    avg_diff = sum(diffs) / len(diffs)
    variance = sum((d - avg_diff)**2 for d in diffs) / len(diffs)
    stability = 1 / (1 + variance)
    return round(stability, 6)

# Irrelevant helper - dead code path (decoy)
def unused_fourier_approximation(data, terms=3):
    result = []
    for t in range(len(data)):
        val = 0
        for k in range(terms):
            val += math.sin((k+1) * t * math.pi / 4)
        result.append(round(val, 4))
    return result

# Another red herring: complex transformation not used in final calculation
def generate_synthetic_baseline(length, seed=42):
    import random
    random.seed(seed)
    return [round(random.gauss(0.5, 0.1), 6) for _ in range(length)]

# Core diagnostic logic
def analyze_metrics(vital_signs, thresholds):
    
    # Step 1: Preprocess the input vector
    processed = preprocess_signal(vital_signs)
    
    # Step 2: Compute derived metrics
    entropy_measure = compute_entropy(processed)
    stability_score = evaluate_stability_index(processed)
    has_spike_rhythm = detect_spike_pattern(processed)
    
    # Step 3: Extract threshold parameters
    base_threshold = thresholds['primary']
    adaptive_floor = thresholds['secondary'] * stability_score
    
    # Step 4: Conditional adjustment based on pattern detection
    if has_spike_rhythm:
        base_threshold *= 0.85
    else:
        base_threshold *= 1.1
    
    # Step 5: Weighted combination using conditional expression
    risk_numerator = entropy_measure * (2 if has_spike_rhythm else 1.5)
    
    # Step 6: Apply dynamic scaling
    dynamic_factor = stability_score ** 2 + 0.1
    
    # Step 7: Main diagnostic index calculation
    diagnostic_index = (risk_numerator / (dynamic_factor + adaptive_floor))
    
    # Step 8: Final adjustment via conditional expression
    final_value = diagnostic_index if diagnostic_index > base_threshold else (base_threshold + diagnostic_index) / 2
    
    return round(final_value, 6)

# Simulation data setup
raw_vitals = [0.15, 0.82, 0.12, 0.91, 0.08, 0.87, 0.11, 0.79, 0.21, 0.18]

threshold_config = {
    'primary': 0.42,
    'secondary': 0.35,
    'tertiary': 0.6  # Unused parameter - distraction
}

# Dead code assignment - irrelevant
baseline_sim = generate_synthetic_baseline(len(raw_vitals))
fourier_test = unused_fourier_approximation(raw_vitals)

# Key computation
final_diagnostic = analyze_metrics(raw_vitals, threshold_config)

# Print result as required
print(f"Target result: {final_diagnostic}")