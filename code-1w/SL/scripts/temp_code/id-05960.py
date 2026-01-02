import math

def collect_diagnostics():
    # Simulated sensor metrics from a distributed system
    raw_readings = [14.2, 18.5, 23.1, 9.7, 31.4, 27.8, 11.6, 19.3, 25.0, 16.7]
    
    # Irrelevant transformation: convert to string lengths (distraction)
    str_lengths = [len(str(x)) for x in raw_readings]
    avg_str_length = sum(str_lengths) / len(str_lengths)
    
    # Baseline thresholds defined as a set for efficient lookup
    baseline_set = {10, 15, 20, 25, 30}
    
    # Outlier detection using deviation threshold (red herring)
    mean_val = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_val) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)
    outlier_threshold = mean_val + 1.5 * std_dev
    
    # Actual filtering logic: values > 20 and not close to any baseline
    def is_significant(x):
        return x > 20 and not any(abs(x - b) < 2 for b in baseline_set)
    
    filtered_metrics = [x for x in raw_readings if is_significant(x)]
    
    # Decoy function: looks important but unused
    def compute_entropy(data):
        freq_map = {}
        for d in data:
            freq_map[d] = freq_map.get(d, 0) + 1
        probabilities = [f / len(data) for f in freq_map.values()]
        return -sum(p * math.log2(p) for p in probabilities)
    
    # Another distraction: simulate redundant health check
    system_health_flags = []
    for val in raw_readings:
        if val < 12:
            system_health_flags.append('WARNING')
        elif val > 28:
            system_health_flags.append('CRITICAL')
        else:
            system_health_flags.append('OK')
    
    # Dead code path: never executed due to prior filtering
    legacy_correction = 0
    if 'DEBUG_MODE' in globals():
        for i in range(len(raw_readings)):
            legacy_correction += raw_readings[i] % 7

    # Core analysis function with multiple steps
    def analyze_readings(readings, base_set):
        if not readings:
            return 0
        
        # Step 1: map each reading to its distance from nearest baseline
        distances = []
        for r in readings:
            nearest = min(base_set, key=lambda x: abs(r - x))
            distances.append(abs(r - nearest))
        
        # Step 2: apply non-linear penalty for large deviations
        penalties = [math.exp(d / 5) for d in distances]
        
        # Step 3: aggregate via harmonic mean (more sensitive to small values)
        if not penalties:
            return 0
        inv_sum = sum(1 / p for p in penalties)
        harmonic_penalty = len(penalties) / inv_sum
        
        # Step 4: adjust by count of readings above secondary threshold
        adjustment_factor = sum(1 for r in readings if r > 24)
        
        # Step 5: use set intersection to detect anomalies (core relevance)
        ceiling_limit = 35
        soft_bounds = set(range(20, 31))
        reading_ints = set(int(r) for r in readings)
        overlap_count = len(reading_ints & soft_bounds)
        
        # Final computation chain
        intermediate = harmonic_penalty * adjustment_factor
        final_score = intermediate + overlap_count
        
        # Distraction: unused alternate formula
        alt_formula = math.log(sum(penalties)) * len(reading_ints & {24, 25, 26})
        
        return int(final_score)

    # Key execution point
    final_diagnostic = analyze_readings(filtered_metrics, baseline_set)
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    collect_diagnostics()