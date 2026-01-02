import itertools

def analyze_pattern(sequence):
    trend = 0
    noise_floor = 0.05
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        if abs(diff) > noise_floor:
            trend += int(diff * 10)
    return trend

def validate_signal(strength):
    return 0 < strength < 100 and strength % 2 == 1

def calculate_performance(data):
    baseline = sum(data) / len(data)
    adjusted_values = [x - baseline + 2 for x in data]
    
    # Irrelevant transformation (distractor)
    temp_buffer = [x ** 0.5 for x in adjusted_values if x > 0]
    temp_buffer = temp_buffer[::-1]  # slicing - irrelevant reversal
    
    # Key processing
    filtered = [x for x in adjusted_values if validate_signal(int(abs(x)))]
    pattern_trend = analyze_pattern(filtered)
    
    # Secondary distractor: unused statistical calculation
    variance_proxy = sum((x - baseline) ** 2 for x in data) / len(data) if data else 0
    entropy_approx = 0
    for v in filtered:
        if v != 0:
            entropy_approx += abs(v) * 0.1

    # Conditional expression with bitwise twist
    score_modifier = 7 if len(filtered) > 3 else 3
    final_score = int(abs(pattern_trend) * score_modifier)
    
    # Additional red herring: XOR-based checksum (unused)
    checksum = 0
    for val in data:
        checksum ^= int(val) % 17
    
    return final_score

# Main execution
benchmark_data = [4.2, 5.1, 3.9, 6.3, 5.8, 4.7]
interim_result = [x * 1.1 for x in benchmark_data]  # dead path
normalization_factor = sum(interim_result) / 100  # unused normalization

final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")