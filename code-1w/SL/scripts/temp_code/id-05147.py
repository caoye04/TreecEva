import itertools

# Simulated sensor array processing with diagnostic evaluation
def analyze_sensor_cluster(raw_readings, threshold_config):
    # Irrelevant transformation: normalize readings (not used in final path)
    normalized = [round(x / max(raw_readings), 3) for x in raw_readings]
    
    # Distractor: complex but unused frequency analysis
    fft_proxy = [abs((i - len(raw_readings)//2)**2 - i) for i in range(len(raw_readings))]
    spectral_weight = sum(fft_proxy[:5]) if len(fft_proxy) > 5 else 0

    # Key signal filtering based on dynamic thresholds
    activation_mask = [1 if x > threshold_config['upper'] or x < threshold_config['lower'] else 0 for x in raw_readings]
    
    # Red herring: entropy-like calculation with no impact
    bit_entropy = 0
    for i in range(len(activation_mask) - 1):
        if activation_mask[i] != activation_mask[i+1]:
            bit_entropy += 0.17
    
    # Real computation: extract high-variance segments
    segments = []
    start = None
    for idx, val in enumerate(activation_mask):
        if val == 1 and start is None:
            start = idx
        elif val == 0 and start is not None:
            segments.append((start, idx))
            start = None
    if start is not None:
        segments.append((start, len(activation_mask)))

    # Distractor: unused segment compression attempt
    compressed_refs = []
    for s in segments:
        if s[1] - s[0] > 2:
            compressed_refs.append((s[0], s[1], 'FLAG'))

    # Core logic: derive signal quality score from segment density
    if not segments:
        return 0.0
    
    total_exposure = sum(end - start for start, end in segments)
    quality_score = round(total_exposure * 1.75 / len(raw_readings), 4)
    return quality_score


def transform_basis_vectors(vector_set):
    # Unused mathematical transformation (decoy function)
    rotated = []
    for v in vector_set:
        x, y = v
        rotated.append((x*0.866 - y*0.5, x*0.5 + y*0.866))
    return rotated

def generate_synthetic_sequence(length, seed=123):
    # Pseudo-random sequence generator (misleading but deterministic)
    seq = [seed % 97]
    for _ in range(1, length):
        seq.append((seq[-1] * 7 + 13) % 101)
    return [x % 10 for x in seq]

# Main execution block simulating diagnostic pipeline
if __name__ == '__main__':
    # Input data - sensor readings from environmental monitoring array
    primary_readings = [0.4, 1.8, 0.9, 2.3, 0.1, 0.7, 1.1, 2.5, 2.6, 0.3, 1.0, 0.2, 2.4]
    
    # Configuration map (some fields are red herrings)
    config = {
        'upper': 2.0,
        'lower': 0.5,
        'gain': 1.25,
        'window': 7,
        'mode': 'adaptive'
    }
    
    # Step 1: Analyze clusters (only this matters)
    diagnostic_1 = analyze_sensor_cluster(primary_readings, config)
    diagnostic_2 = analyze_sensor_cluster(primary_readings[3:], config)
    diagnostic_3 = analyze_sensor_cluster(primary_readings[:8], config)
    
    # Step 2: Generate irrelevant synthetic control group
    synthetic_baseline = generate_synthetic_sequence(15, seed=42)
    control_flag = any(x > 8 for x in synthetic_baseline)  # Dead-end logic
    
    # Step 3: Prepare signal reduction using Cartesian product (itertools usage)
    reduced_signals = []
    for a, b in itertools.product([diagnostic_1], [diagnostic_2, diagnostic_3]):
        reduced_signals.append(round((a + b) * 0.6, 4))
    
    # Step 4: Baseline offset computed from unused vector transform
    dummy_vectors = [(2, 3), (1, -1), (0, 4)]
    transformed = transform_basis_vectors(dummy_vectors)
    vector_magnitude = sum(abs(p[0]) + abs(p[1]) for p in transformed)  # Distractor
    baseline_offset = len(transformed) * 0.1  # Only this derived value is used
    
    # Step 5: Aggregate final metrics - THIS IS THE KEY STATEMENT
    def aggregate_metrics(metrics, offset):
        if not metrics:
            return 0.0
        raw_total = sum(metrics)
        adjusted = raw_total + offset * 1.5
        
        # Fake branching: uses variables not connected to output
        temp_caps = [min(m, 1.0) for m in metrics]
        if len(temp_caps) > 2:
            adjusted -= 0.05  # Never reached due to input size
        
        return round(adjusted * 2.0, 4)
    
    final_diagnostic = aggregate_metrics(reduced_signals, baseline_offset)
    
    # Output target result
    print(f"Result: {final_diagnostic}")