def analyze_purity(elements):
    return {e for e in elements if e > 0.8}


def normalize_readings(readings):
    max_val = max(readings)
    return [round(r / max_val, 6) for r in readings]


def compute_entropy(data):
    # Irrelevant complexity: computes Shannon entropy but not used in final result
    from math import log2
    total = sum(data)
    probabilities = [d / total for d in data]
    return -sum(p * log2(p) for p in probabilities if p > 0)


def filter_outliers(values, limit=3.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= limit * std_dev]


def adjust_calibration(signal):
    # Decoy transformation
    calibrated = []
    for s in signal:
        if s < 0.1:
            calibrated.append(s * 10)
        elif s > 0.9:
            calibrated.append(0.9)
        else:
            calibrated.append(s)
    return calibrated


def detect_interference(signal_data):
    # Dead-end analysis with misleading intermediate
    interference_flags = []    
    for i, val in enumerate(signal_data):
        flag = (i % 5 == 0 and val < 0.25) or (val > 0.75 and i % 3 == 0)
        interference_flags.append(flag)
    return any(interference_flags)


def aggregate_metrics(samples):
    # Unused aggregation function — red herring
    totals = []
    for sample in samples:
        totals.append(sum(sample.values()))
    return sum(totals) / len(totals) if totals else 0


def evaluate_stability(levels):
    # Complex but irrelevant stability check
    if len(levels) < 2:
        return True
    diffs = [abs(levels[i] - levels[i+1]) for i in range(len(levels)-1)]
    return all(d < 0.1 for d in diffs)


def process_contaminants(water_samples, threshold_levels):
    # Core logic begins here — 8-12 steps with interdependencies
    combined = []
    for sample in water_samples:
        # Extract metal concentrations
        metals = [sample[k] for k in ['lead', 'mercury', 'arsenic'] if k in sample]
        normalized_metals = normalize_readings(metals)
        
        # Apply dynamic thresholds
        filtered = []
        for i, val in enumerate(normalized_metals):
            if val >= threshold_levels[i]:
                filtered.append(val)
        
        # Bit manipulation as noise
        mask = 0b101
        masked_sum = sum(filtered) ^ mask if filtered else 0
        
        # Conditional expression usage
        safety_flag = 'high' if len(filtered) >= 2 else 'moderate'
        
        # Use of dictionary and conditional inclusion
        stats = {
            'raw_sum': round(sum(metals), 6),
            'normalized_sum': round(sum(normalized_metals), 6),
            'filtered_count': len(filtered),
            'status': safety_flag
        }
        
        # Only one field contributes to final score
        combined.append(stats['normalized_sum'])
    
    # Final transformation chain
    valid_results = [c for c in combined if c > 0.5]
    if not valid_results:
        return 0
    
    # Key computation step
    base_score = sum(valid_results)
    adjustment_factor = 0.87
    
    # Early return decoy — not triggered
    if base_score < 0.1:
        return -1
    
    # Final answer calculation
    filtration_score = int(round(base_score * adjustment_factor * 100))
    
    # Additional distraction
    checksum = sum([filtration_score >> i for i in range(0, 8, 2)]) & 0xFF
    
    return filtration_score

# Main execution block
if __name__ == '__main__':
    # Input data setup
    water_samples = [
        {'lead': 0.92, 'mercury': 0.86, 'arsenic': 0.78},
        {'lead': 0.81, 'mercury': 0.95, 'arsenic': 0.67},
        {'lead': 0.73, 'mercury': 0.88, 'arsenic': 0.91}
    ]
    
    threshold_levels = [0.85, 0.90, 0.80]
    
    # Irrelevant preprocessing
    purified = adjust_calibration([s['lead'] for s in water_samples])
    entropy = compute_entropy([s['mercury'] for s in water_samples])
    stable = evaluate_stability(purified)
    
    # Critical call
    filtration_score = process_contaminants(water_samples, threshold_levels)
    
    # Output result
    print(f"Result: {filtration_score}")