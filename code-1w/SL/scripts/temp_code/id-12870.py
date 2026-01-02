import math

def analyze_pulse(sequence, limit):
    peak = 0
    for i in range(len(sequence)):
        if sequence[i] > limit:
            peak += (sequence[i] % 7) * 2
    return peak

def compute_entropy(data):
    # Irrelevant entropy computation (dead function)
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

def extract_features(raw):
    features = set()
    temp_vals = []
    for item in raw:
        temp_vals.append(item ** 2 + 3)
    cutoff = sum(temp_vals) // len(temp_vals)
    for val in temp_vals:
        if val > cutoff:
            features.add(val % 13)
    return features

def filter_anomalies(stream, baseline):
    anomalies = []
    for idx, point in enumerate(stream):
        adjusted = point - (idx * 0.5)
        if abs(adjusted) > baseline and idx % 2 == 0:
            anomalies.append(int(adjusted))
    # Dead code path — never used
    if len(anomalies) > 10:
        anomalies = anomalies[:10]
    return anomalies

def integrate_diagnostics(signals):
    cumulative = 0
    for s in signals:
        if isinstance(s, list):
            inner_sum = 0
            for x in s:
                inner_sum += x % 100
            cumulative += inner_sum // 2
        else:
            cumulative += s // 5
    return cumulative

def aggregate_metrics(signal_set, threshold):
    primary_score = 0
    secondary_score = 0
    
    # Real computation path
    for group in signal_set:
        group_total = sum(group)
        if group_total > threshold:
            primary_score += group_total // threshold
        else:
            primary_score -= 1
    
    # Distractor: irrelevant calculation
    avg_len = sum(len(g) for g in signal_set) / len(signal_set)
    adjustment = int(avg_len * 1.5) if avg_len > 2 else 0
    
    # More distraction: unused intermediate values
    potential_outliers = [g for g in signal_set if max(g) - min(g) > 50]
    outlier_count = len(potential_outliers) * 2  # Not used
    
    # Another red herring: complex but unused transformation
    transformed = set()
    for seq in signal_set:
        for val in seq:
            transformed.add((val * 3 + 7) % 23)
    
    # Actual logic continues here
    secondary_score = len(signal_set) * 4
    
    # Final combination
    final_score = primary_score * 2 + secondary_score - adjustment
    
    # Key variable assignment
    final_diagnostic = final_score
    
    # Additional noise: unrelated print simulation
    debug_state = {"status": "OK", "level": 3, "flags": []}
    debug_state["flags"].append("DIAGNOSTIC_PASS")
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    
    # Input data initialization
    raw_input = [12, 15, 8, 23, 7, 19]
    base_signal = [x * 2 + 1 for x in raw_input]
    
    # Unused derived signals
    harmonic_series = [i * i for i in range(1, 6)]
    phase_shifted = [x + 5 for x in base_signal if x % 3 != 0]
    
    # Construct nested signal structure (used)
    nested_signals = [
        [base_signal[0], base_signal[1], 45],
        [17, 89, 102, 33],
        [54, 21],
        [77, 66, 55, 44, 33]
    ]
    
    # Irrelevant set operations (distractors)
    unique_codes = set(base_signal)
    legacy_codes = set([10, 20, 30, 40])
    active_codes = unique_codes.difference(legacy_codes)
    sync_code = sum(active_codes.intersection({15, 25, 35}))  # Unused
    
    # Threshold derived from modular arithmetic
    system_threshold = (len(base_signal) * 7) % 101
    system_threshold += 25  # Final threshold = 39 + 25 = 64
    
    # Critical call
    final_diagnostic = aggregate_metrics(nested_signals, system_threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")