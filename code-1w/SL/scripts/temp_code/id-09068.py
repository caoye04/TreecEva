from collections import defaultdict, Counter
import math

# Simulated sensor data and system telemetry
def generate_telemetry():
    return [i * 1.5 + (i % 7) * 0.3 for i in range(20)]

def analyze_pattern(seq):
    # Irrelevant pattern analysis (red herring)
    freq = Counter(seq)
    modes = [k for k, v in freq.items() if v == max(freq.values())]
    return sorted(modes)

def deprecated_checksum(data):
    # Unused function — dead code path
    return sum(data) % 1000

def shift_sequence(seq, offset=3):
    # Misleading transformation
    return [x * 1.1 + offset for x in seq[:10]]

def compute_entropy(values):
    # Real but indirect contributor: used to influence threshold
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs if p > 0)

def extract_critical_band(data):
    # Extracts every 3rd element — actually used later
    return [data[i] for i in range(2, len(data), 3)]

def filter_outliers(series, factor=1.5):
    # Dead code — never called
    q1, q3 = np.percentile(series, [25, 75])  # Note: np not imported — would fail
    iqr = q3 - q1
    return [x for x in series if q1 - factor * iqr <= x <= q3 + factor * iqr]

def derive_key_signal(raw):
    # Core signal extraction (used)
    shifted = [x - 1.8 for x in raw]
    powered = [math.pow(x, 2) for x in shifted]
    return powered

def assess_coherence(signal):
    # Determines coherence score (used in final step)
    avg = sum(signal) / len(signal)
    deviations = [abs(x - avg) for x in signal]
    return 1 / (1 + sum(deviations) / len(deviations))

def validate_structure(arr):
    # Superfluous validation
    return all(isinstance(x, float) and x >= 0 for x in arr)

def normalize_readings(readings):
    # Actually used normalization
    min_val, max_val = min(readings), max(readings)
    if max_val == min_val:
        return [0.0] * len(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

def aggregate_diagnostics(metrics):
    # Aggregation logic with decoy branches
    base_score = sum(metrics.get('readings', []))
    adjustment = metrics.get('coherence', 0)
    penalty = 0
    if len(metrics.get('readings', [])) > 10:
        penalty += 2.5
    if metrics.get('entropy') > 2.0:  # This will be true
        penalty -= 0.8  # Counterintuitive: reduces penalty
    return base_score * adjustment - penalty

def process_metrics(trace, load):
    # Main processing pipeline
    segment_a = trace[::2]
    segment_b = extract_critical_band(trace)  # Actual usage
    signal_raw = derive_key_signal(segment_b)
    normalized = normalize_readings(signal_raw)
    entropy = compute_entropy(trace)
    coherence = assess_coherence(normalized)
    
    # Dummy assignments to mislead
    audit_log = defaultdict(int)
    audit_log['stage_1'] = len(segment_a)
    audit_log['stage_2'] = len(segment_b)
    audit_log['anomaly_flag'] = False
    
    temp_result = [x * coherence for x in normalized]
    capped = [min(x, 0.95) for x in temp_result]
    
    metrics_bundle = {
        'readings': capped,
        'coherence': coherence,
        'entropy': entropy,
        'size': len(trace)
    }
    
    # Final computation chain
    raw_diagnostic = aggregate_diagnostics(metrics_bundle)
    adjustment_factor = 1.0
    if coherence > 0.5:
        adjustment_factor *= 1.2
    final_diagnostic = int(round(raw_diagnostic * adjustment_factor))
    return final_diagnostic

# --- Simulation Entry Point ---
if __name__ == "__main__":
    # Generate core data
    health_trace = generate_telemetry()  # Base sequence
    system_load = [x ** 0.5 for x in range(20, 40)]  # Distractor data
    
    # Irrelevant pre-processing
    processed_load = [x + 0.1 for x in system_load]
    load_stats = {"mean": sum(processed_load) / len(processed_load)}
    
    # Key execution point
    final_diagnostic = process_metrics(health_trace, system_load)
    
    # Print required result
    print(f"Result: {final_diagnostic}")