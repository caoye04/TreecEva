import itertools

# Simulated sensor data processing with diagnostic analysis
def collect_telemetry():
    raw_readings = [18, 22, 15, 30, 12, 25, 14]
    adjustment_factor = 0.85
    filtered = [x for x in raw_readings if x > 13]
    adjusted = [round(x * adjustment_factor) for x in filtered]
    return adjusted

def compute_volatility(sequence):
    if len(sequence) < 2:
        return 0
    diffs = [abs(a - b) for a, b in zip(sequence, sequence[1:])]
    volatility = sum(diffs) / len(diffs)
    return volatility

def generate_synthetic_series(length):
    # Distractor: generates unused synthetic pattern
    return [i ** 2 % 17 for i in range(length)]

def evaluate_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    threshold = 25.0
    stability_score = 1 if variance < threshold else 0
    return stability_score

def apply_correction(data, mode=2):
    # Irrelevant correction path (not used in final result)
    if mode == 1:
        return [x + 1 for x in data]
    elif mode == 2:
        return [x - 1 for x in data]
    else:
        return data

def aggregate_metrics(data, offset):
    base = sum(data)
    shift = offset ** 2
    # Core logic: combine shifted offset with product of non-zero even elements
    even_elements = [x for x in data if x % 2 == 0 and x != 0]
    if not even_elements:
        product = 1
    else:
        product = 1
        for x in even_elements:
            product *= x
    # Real computation path
    result = base + shift - (product % 19)
    return result

def main():
    # Step 1: Collect real data
    sensor_output = collect_telemetry()
    
    # Step 2: Compute volatility (used later)
    trend_data = sorted(sensor_output, reverse=True)
    current_volatility = compute_volatility(trend_data)
    
    # Step 3: Evaluate system stability (distractor variable)
    system_stable = evaluate_stability(trend_data)
    
    # Step 4: Generate unused synthetic series (red herring)
    fake_pattern = generate_synthetic_series(50)
    fake_avg = sum(fake_pattern) / len(fake_pattern)
    
    # Step 5: Apply irrelevant correction (dead code path)
    corrected_data = apply_correction(trend_data, mode=3)
    
    # Step 6: Calculate baseline offset using volatility
    baseline_offset = int(current_volatility)
    
    # Step 7: Misleading intermediate calculation (not used)
    temp_diagnostic = (baseline_offset * 2) + system_stable
    temp_diagnostic = temp_diagnostic if temp_diagnostic > 10 else 0
    
    # Step 8: Key statement - this determines the actual answer
    final_diagnostic = aggregate_metrics(trend_data, baseline_offset)
    
    # Step 9: Additional red herring using itertools
    permutations_count = 0
    for _ in itertools.permutations([1, 2, 3], 3):
        permutations_count += 1  # Always 6, irrelevant
    scaling_noise = permutations_count * fake_avg
    
    # Step 10: Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()