def analyze_readings(readings):
    processed = []
    for i, val in enumerate(readings):
        if i % 2 == 0:
            processed.append(val * 1.5)
        else:
            processed.append(val + 2.0)
    return [round(p, 2) for p in processed]

# Irrelevant helper (dead function - decoy)
def normalize_data(data):
    mean = sum(data) / len(data)
    return [(x - mean) / mean for x in data]

# Misleading transformation chain
def transform_signal(signal):
    shifted = [x << 2 for x in signal if isinstance(x, int)]
    wrapped = zip(shifted[::2], shifted[1::2])
    combined = [a ^ b for a, b in wrapped]
    return combined  # Never used

# Core logic obscured by noise
def evaluate_stability(metrics, config=None):
    base_score = 0
    decoy_accum = 0
    
    for idx, (name, val) in enumerate(zip(['alpha', 'beta', 'gamma', 'delta'], metrics)):
        if val > 85:
            base_score += 3
        elif val > 70:
            base_score += 2
        else:
            base_score += 1
        
        # Red herring computation
        decoy_accum += (idx + 1) * (val % 10) ** 2
    
    # Actual relevant result
    return base_score

# Complex recursive filter (partially relevant)
def filter_outliers(seq, limit=3):
    if limit == 0 or len(seq) < 2:
        return seq
    
    avg = sum(seq) / len(seq)
    deviants = {i for i, x in enumerate(seq) if abs(x - avg) > 0.5 * avg}
    
    if not deviants:
        return seq
    
    filtered = [x for i, x in enumerate(seq) if i not in deviants]
    return filter_outliers(filtered, limit - 1)

# Unused complex structure (distractor)
class DiagnosticCache:
    def __init__(self):
        self.entries = {}
        self.audit_log = []

    def log_access(self, key, value):
        self.audit_log.append((key, value))

    def clear(self):
        self.entries.clear()

# Main diagnostic engine
def compute_diagnostic(metrics, threshold_map):
    # Step 1: Preprocess with conditional scaling
    adjusted = [m * 1.1 if m < threshold_map['warning'] else m * 0.9 for m in metrics]
    
    # Step 2: Analyze pattern stability
    stability = evaluate_stability(adjusted)
    
    # Step 3: Detect spikes (bit manipulation red herring)
    spike_mask = 0
    for v in adjusted:
        if v > threshold_map['critical']:
            spike_mask |= (1 << int(v) % 8)  # Decoy bitmask
    
    # Step 4: Filter noise from readings
    clean_metrics = filter_outliers([int(x) for x in adjusted if x > 0])
    
    # Step 5: Compute entropy-like measure (simplified)
    from math import log2
    freq = {}
    for x in clean_metrics:
        freq[x] = freq.get(x, 0) + 1
    entropy = sum(-(count / len(clean_metrics)) * log2(count / len(clean_metrics)) for count in freq.values())
    
    # Step 6: Apply correction based on stability
    if stability >= 9:
        adjustment_factor = 1.25
    elif stability >= 6:
        adjustment_factor = 1.0
    else:
        adjustment_factor = 0.75
    
    # Step 7: Final integration
    raw_sum = sum(clean_metrics)
    intermediate = raw_sum * adjustment_factor * (1 + entropy)
    
    # Step 8: Final diagnostic score
    final_diagnostic = int(intermediate + 0.5)  # Round to nearest int
    
    # Irrelevant logging (distraction)
    debug_state = {'step': 'final', 'temp_var': raw_sum ^ int(entropy)}
    
    return final_diagnostic

# Execution setup
health_metrics = [68, 73, 88, 92, 65, 77, 81]
thresholds = {
    'baseline': 60,
    'warning': 75,
    'critical': 85
}

# Dead code path (never called)
def generate_report():
    return "Full diagnostics pending..."

# Trigger main computation
final_diagnostic = compute_diagnostic(health_metrics, thresholds)
print(f"Result: {final_diagnostic}")