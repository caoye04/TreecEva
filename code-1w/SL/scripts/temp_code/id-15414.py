import itertools

def analyze_response_time(raw_times, threshold=0.5):
    # Irrelevant analysis function (dead code path)
    return [t for t in raw_times if t > threshold]

def preprocess_metrics(data_stream):
    # Distractor: complex but unused data transformation
    cleaned = []
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            cleaned.append(val * 1.1)
        else:
            cleaned.append(val + 0.05)
    return [round(x, 3) for x in cleaned]

def evaluate_stability(readings):
    # Misleading intermediate result
    baseline = sum(readings) / len(readings)
    variance = sum((x - baseline) ** 2 for x in readings) / len(readings)
    return variance < 0.08

def compute_adaptive_weight(iteration, max_iter=10):
    # Relevant but obfuscated weight calculation
    if iteration < max_iter // 2:
        return 0.6
    else:
        return 0.9 - (iteration - max_iter // 2) * 0.05

def generate_feedback_pattern(n):
    # Creates pattern using zip and enumerate (red herring)
    indices = list(range(n))
    shifts = [(i * 2) % n for i in range(n)]
    pairs = list(zip(indices, shifts))
    pattern = [a ^ b for a, b in pairs]
    return [p % 4 for p in pattern]

def simulate_calibration_cycle(initial_val, cycles):
    # Unused simulation with bit manipulation distraction
    result = initial_val
    for i in range(cycles):
        temp = (result << 2) ^ (result >> 1)
        result = (temp + i) & 0xFF
    return result

def aggregate_performance(feedback_cycles):
    cumulative = 0.0
    weights = [compute_adaptive_weight(i, len(feedback_cycles)) for i in range(len(feedback_cycles))]
    
    # Core logic embedded within distractions
    for idx, cycle_data in enumerate(feedback_cycles):
        raw_value = cycle_data['base']
        adjustment_factor = cycle_data['factor']
        
        # Real computation buried here
        adjusted = raw_value * adjustment_factor
        
        # This condition is actually critical
        if idx % 2 == 1:
            adjusted = adjusted ** 0.5  # Square root applied only on odd indices
        
        weighted_contribution = adjusted * weights[idx]
        cumulative += weighted_contribution
    
    # Final transformation
    final = cumulative * 100 // 1 * 1.0  # Floor then convert to float
    
    # Decoy operation that looks important
    checksum = sum(1 for x in weights if x > 0.7)
    offset = len([x for x in itertools.combinations(range(5), 2)])  # Constant = 10
    
    # Actual answer unaffected by checksum/offset
    return int(final)  # Deterministic integer output

# Main execution block
if __name__ == '__main__':
    # Simulated input data
    feedback_cycles = [
        {'base': 0.12, 'factor': 1.5},
        {'base': 0.25, 'factor': 2.0},
        {'base': 0.18, 'factor': 1.8},
        {'base': 0.22, 'factor': 2.2},
        {'base': 0.15, 'factor': 1.6}
    ]
    
    # Irrelevant preprocessing
    timestamps = [0.45, 0.67, 0.33, 0.89, 0.51]
    filtered = analyze_response_time(timestamps)
    processed = preprocess_metrics(timestamps)
    stable = evaluate_stability(processed)
    
    # Generate unused patterns
    pattern = generate_feedback_pattern(5)
    calibration = simulate_calibration_cycle(0x1A, 8)
    
    # Key statement
    final_score = aggregate_performance(feedback_cycles)
    
    # Output result
    print(f"Result: {final_score}")