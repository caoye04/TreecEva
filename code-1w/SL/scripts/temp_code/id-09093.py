import math

# Simulated sensor calibration data and fault detection system
def generate_calibration_sequence():
    base_values = [i * 3.7 for i in range(15)]
    noise_offset = [(i % 3 - 1) * 0.21 for i in range(15)]
    return [base_values[i] + noise_offset[i] for i in range(15)]

# Irrelevant helper: simulates temperature drift (not actually used in final result)
def simulate_drift(values, factor=0.08):
    return [v * (1 + factor * (i - len(values)//2)) for i, v in enumerate(values)]

# Misleading fault detector with decoy logic
def legacy_fault_scan(data):
    anomalies = []
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) > 4.0:  # Threshold never triggered
            anomalies.append(i)
    return anomalies  # Dead end – not used in correct path

# Core diagnostic processor
sensitivity_map = {i: math.cos(i * 0.1) ** 2 for i in range(15)}

def compute_weighted_residuals(seq):
    residuals = []
    for i, val in enumerate(seq):
        expected = i * 3.7
        residual = abs(val - expected)
        weighted = residual * sensitivity_map[i]
        residuals.append(weighted)
    return residuals

# Advanced filter using lambda and set operations
def filter_significant_indices(residuals):
    threshold = sum(residuals) / len(residuals) * 1.15
    significant_set = {i for i, r in enumerate(residuals) if r > threshold}
    outlier_filter = lambda idx: idx % 2 == 1  # Only odd indices considered unstable
    filtered_set = {idx for idx in significant_set if outlier_filter(idx)}
    return filtered_set

# Fault line analyzer with red herring computation
def analyze_fault_patterns(indices, sequence):
    # Meaningless aggregation
    phantom_sum = sum(math.tanh(sequence[i]) for i in range(0, len(sequence), 3))
    
    # Actual relevant logic
    if len(indices) == 0:
        return [0]
    sorted_indices = sorted(list(indices))
    gaps = [sorted_indices[i] - sorted_indices[i-1] for i in range(1, len(sorted_indices))]
    return [len(indices), sum(gaps) if gaps else 0]

# Data transformation pipeline with distraction
transformation_chain = [
    lambda x: x + 1.1,
    lambda x: x * 0.95,
    lambda x: x if x > 5 else x * 1.2  # Not ultimately used
]

# Main processing function
def process_metrics(raw_data, debug_mode=False):
    # Step 1: Clean data
    cleaned = [round(x, 3) for x in raw_data]
    
    # Step 2: Compute residuals
    residuals = compute_weighted_residuals(cleaned)
    
    # Step 3: Identify critical indices
    critical_indices = filter_significant_indices(residuals)
    
    # Step 4: Analyze pattern (only first two elements matter)
    pattern_vector = analyze_fault_patterns(critical_indices, cleaned)
    
    # Step 5: Generate diagnostic hash (distraction)
    diagnostic_hash = sum(i * p for i, p in enumerate(pattern_vector)) * 1000
    
    # Step 6: Final diagnostic score (ACTUAL ANSWER)
    # Formula: pattern_vector[0] * 100 + pattern_vector[1] * 10 + length of critical_indices
    intermediate = pattern_vector[0] * 100 + pattern_vector[1] * 10
    final_score = intermediate + len(critical_indices)
    
    # Irrelevant logging
    if debug_mode:
        print(f'Debug: {diagnostic_hash}')
        
    return final_score

# Execution flow
if __name__ == '__main__':
    # Primary data source
    calibration_sequence = generate_calibration_sequence()
    
    # Decoy call to legacy system
    fault_lines = legacy_fault_scan(calibration_sequence)  # Returns empty list, but looks important
    
    # Critical assignment - this is the key execution point
    final_diagnostic = process_metrics(calibration_sequence, fault_lines)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")