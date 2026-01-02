import math

def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    squared_energy = sum([x**2 for x in filtered])
    return squared_energy / len(filtered) if filtered else 0.0

def detect_spikes(values, sensitivity=1.5):
    spikes = []
    for i in range(1, len(values)-1):
        if values[i] > sensitivity * (values[i-1] + values[i+1]) / 2:
            spikes.append(i)
    return spikes

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return entropy

def generate_baseline(n):
    return [math.sin(i * 0.5) + 0.1 * math.cos(i * 3) for i in range(n)]

def transform_sequence(seq):
    # Irrelevant transformation chain
    temp_a = [x * 1.5 + 2 for x in seq]
    temp_b = [abs(y) ** 0.5 for y in temp_a]
    temp_c = [round(z, 2) for z in temp_b]
    shifted = [temp_c[-i % len(temp_c)] for i in range(len(temp_c))]
    return shifted

def evaluate_stability(indices):
    if not indices:
        return 0
    diffs = [indices[i+1] - indices[i] for i in range(len(indices)-1)]
    return sum(diffs) / len(diffs) if diffs else 0

def aggregate_metrics(data, config):
    trend_strength = sum(data) / len(data)
    volatility = sum([abs(data[i+1] - data[i]) for i in range(len(data)-1)])
    
    # Distractor: complex unused structure
    stats_summary = {
        'peak': max(data),
        'trough': min(data),
        'range': max(data) - min(data),
        'mean': sum(data)/len(data),
        'median': sorted(data)[len(data)//2]
    }
    
    # Another red herring: unused computation
    derived_features = []
    for idx, val in enumerate(data):
        if idx % 3 == 0 and val > 0:
            derived_features.append(math.tanh(val) * idx)
    feature_fusion = sum([f**2 for f in derived_features]) if derived_features else 0
    
    # Key logic path
    threshold_mask = [1 if x > config['upper'] else -1 if x < config['lower'] else 0 for x in data]
    crossings = sum([1 for i in range(1, len(threshold_mask)) if threshold_mask[i] != threshold_mask[i-1]])
    
    # Decoy function call with no side effects
    _ = compute_entropy([int(abs(x*10)) % 4 for x in data])
    
    # Core calculation
    adjustment_factor = 1 + (volatility / (trend_strength + 1e-8))
    base_score = trend_strength * adjustment_factor
    penalty = 0.1 * crossings
    
    # Final result
    final_metric = base_score - penalty
    return round(final_metric, 6)

# --- Main execution ---
if __name__ == '__main__':
    # Generate realistic input (distractor-heavy setup)
    raw_samples = generate_baseline(100)
    processed_signal = transform_sequence(raw_samples)
    spike_indices = detect_spikes(processed_signal, sensitivity=1.2)
    stability_index = evaluate_stability(spike_indices)
    
    # Irrelevant data structures
    audit_log = []
    for i, val in enumerate(processed_signal):
        if i in spike_indices:
            audit_log.append(f"Event at {i}: {val:.3f}")
    
    # Unused statistical analysis
    energy_level = analyze_signal(processed_signal)
    signal_entropy = compute_entropy([int(abs(x)*100) % 10 for x in processed_signal])
    
    # Prepare actual inputs
    trend_data = [math.cos(x * 0.3) * math.exp(-i/100) for i, x in enumerate(processed_signal)]
    
    # Configuration with misleading keys
    thresholds = {
        'upper': 0.45,
        'lower': -0.35,
        'window': 5,
        'hysteresis': 0.1,
        'gain': 1.2
    }
    
    # Dead code branch
    if len(audit_log) > 1000:
        fallback = [x * 0.1 for x in trend_data]
        final_diagnostic = sum(fallback)
    else:
        # Critical statement
        final_diagnostic = aggregate_metrics(trend_data, thresholds)
    
    print(f"Result: {final_diagnostic}")