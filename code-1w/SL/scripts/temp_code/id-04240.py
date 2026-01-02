def analyze_phase(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg, variance


def validate_stability(logs):
    if len(logs) < 3:
        return False
    for i in range(1, len(logs)):
        if abs(logs[i] - logs[i-1]) > 0.5:
            return False
    return True


def calculate_performance(data):
    phase_averages = []
    stability_flags = {}
    temp_cache = {}
    
    for key, values in data.items():
        if 'phase' in key:
            avg, var = analyze_phase(values)
            phase_averages.append(avg)
            
            # Irrelevant caching step
            temp_cache[key] = var * 1.5
            
            # Stability check (semi-relevant)
            stable = validate_stability(values[:5] if len(values) >= 5 else values)
            stability_flags[key] = stable
    
    # Misleading intermediate calculation
    cached_sum = sum(temp_cache.values())
    adjustment_factor = 1.0
    if cached_sum > 10:
        adjustment_factor = 0.95
    
    # Key logic: compute weighted score based on averages and stability
    base_score = sum(phase_averages)
    bonus = 0
    for flag in stability_flags.values():
        if flag:
            bonus += 5
    
    # Distractor: unused loop over zipped indices
    indices_values = list(zip(enumerate(phase_averages), stability_flags.keys()))
    dummy_accum = 0
    for (idx, val), name in indices_values:
        dummy_accum += idx * (val % 2)  # Never used
    
    # Final computation
    final_score = (base_score * adjustment_factor) + bonus
    
    # Another red herring
    outlier_count = 0
    for vals in data.values():
        for v in vals:
            if v < 0.1 or v > 9.9:
                outlier_count += 1
    
    return final_score

# Simulated benchmark data
benchmark_data = {
    'phase_initial': [2.1, 2.3, 2.0, 2.2, 2.1],
    'phase_warmup': [1.9, 2.0, 2.1, 2.0, 1.8],
    'phase_main': [3.5, 3.6, 3.4, 3.5, 3.7, 3.6],
    'phase_final': [4.0, 4.1, 4.0, 3.9]
}

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")