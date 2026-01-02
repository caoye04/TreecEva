from itertools import combinations

def analyze_sequence(seq):
    total_peaks = 0
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            total_peaks += 1
    return total_peaks

def calculate_trend_strength(values):
    # Distractor function: computes trend but not used in final logic
    increases = sum(1 for a, b in zip(values, values[1:]) if b > a)
    decreases = sum(1 for a, b in zip(values, values[1:]) if b < a)
    return (increases - decreases) / len(values) if values else 0

def calculate_performance(data):
    baseline_offset = 17
    adjustment_factor = 0
    peak_count = analyze_sequence(data)
    
    # Real logic starts here
    filtered = [x for x in data if x % 2 == 1]  # keep odd numbers
    temp_result = sum(filtered) // (len(filtered) or 1)
    
    # Irrelevant intermediate calculations
    moving_avg = [sum(data[i:i+3]) / 3 for i in range(len(data)-2)]
    volatility = sum(abs(a-b) for a, b in zip(moving_avg, moving_avg[1:]))
    dummy_pairs = list(combinations(data, 2))  # stored but unused
    
    # Core computation chain
    if temp_result > 50:
        adjustment_factor += 10
    elif temp_result < 30:
        adjustment_factor -= 5
    else:
        adjustment_factor += 3
    
    # Additional distraction: complex but unused conditional expression
    status_flag = 'high' if volatility > 20 else 'low'
    extra_weight = 2 if status_flag == 'high' and len(dummy_pairs) > 10 else 1
    
    # Final score calculation
    raw_score = peak_count * temp_result + adjustment_factor
    scaling_factor = 1.5 if len(filtered) > 4 else 1.0
    final_score = int(raw_score * scaling_factor) + baseline_offset
    
    return final_score

# Main execution
benchmark_data = [12, 15, 23, 18, 27, 35, 29, 44, 33]
intermediate_sum = sum(benchmark_data[:4])  # irrelevant tracking
reference_peak = max(benchmark_data)  # distractor variable
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")