def analyze_signal_strength(signal_sequence, threshold=0.75):
    """
    Analyzes signal strength with false positives and noise filtering.
    This function contains red herrings: peak_count, noise_ratio, and calibration_offset
    are computed but not used in the final result.
    """
    normalized = [x / max(signal_sequence) for x in signal_sequence]
    filtered = [x for x in normalized if x > threshold]
    
    # Distractor: irrelevant computation
    peak_count = sum(1 for i in range(1, len(normalized)-1) if normalized[i-1] < normalized[i] > normalized[i+1])
    noise_ratio = (len(normalized) - len(filtered)) / len(normalized)
    calibration_offset = sum([abs(normalized[i] - normalized[i-1]) for i in range(1, len(normalized))]) * 0.01

    # Actual relevant transformation chain
    significant = [int(x * 100) for x in filtered]
    return significant


def transform_coordinates(coords):
    """
    Transforms geographic coordinates. Another decoy function that is defined but never called.
    """
    transformed = []
    for lat, lon in coords:
        new_lat = (lat + 90) % 180
        new_lon = (lon + 180) % 360
        transformed.append((new_lat, new_lon))
    return transformed


def calculate_entropy(data):
    """
    Calculates Shannon entropy - looks important but unused.
    """
    from math import log2
    total = sum(data)
    probabilities = [d / total for d in data]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def process_time_series(raw_values):
    """
    Processes time-series data with modular arithmetic and conditional filtering.
    """
    # Irrelevant intermediate variables
    baseline = sum(raw_values) / len(raw_values)
    deviation = [abs(x - baseline) for x in raw_values]
    volatility = sum(deviation) / len(deviation)
    
    # Key processing path begins
    adjusted = [(v * 3) % 25 for v in raw_values if v > 0]
    paired = list(zip(adjusted[::2], adjusted[1::2]))  # Use zip
    
    processed = []
    for idx, (a, b) in enumerate(paired):  # Use enumerate
        if idx % 3 == 0:
            processed.append(a + b)
        elif a > b:
            processed.append(a ** 2)
        else:
            processed.append(b - a)
    
    # Injecting dead branch
    if len(processed) > 100:
        processed = processed[:50]
    
    return processed


def compute_final_score(data_chunk):
    """
    Final computation involving bitwise operations and conditional logic.
    """
    score = 0
    temp_results = []
    
    for val in data_chunk:
        # Simulate multiple reasoning paths
        case_a = (val << 2) + 3
        case_b = (val | 7) ^ 5
        case_c = (val * 2) - (val % 4)
        
        # Conditional expression determines which path contributes
        selected = case_a if val < 20 else (case_b if val % 2 == 0 else case_c)
        temp_results.append(selected)
    
    # Secondary transformation
    aggregated = 0
    for i, res in enumerate(temp_results):
        if i % 2 == 0:
            aggregated += res // 2
        else:
            aggregated += res % 19
    
    # Final manipulation using modular arithmetic
    checksum = sum(temp_results) % 1000
    score = (aggregated * 2) - checksum
    
    # Decoy assignment
    final_diagnostics = {
        'count': len(temp_results),
        'peak': max(temp_results) if temp_results else 0,
        'debug_flag': False
    }
    
    return score

# Main execution block
if __name__ == '__main__':
    # Input data - realistic sensor readings
    raw_input = [12, -5, 8, 0, 15, 22, -3, 7, 18, 25, 4, 9]
    
    # Step 1: Process through signal analysis (redundant call for distraction)
    dummy_signal = analyze_signal_strength([0.1, 0.8, 0.6, 0.92, 0.76, 0.81])
    
    # Step 2: Real data processing begins here
    processed_data = process_time_series(raw_input)
    
    # Step 3: Compute final score — this is the key statement
    final_score = compute_final_score(processed_data)
    
    # Output result as required
    print(f"Result: {final_score}")