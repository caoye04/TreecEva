from itertools import combinations

def analyze_sequence(seq):
    total_peaks = 0
    temp_buffer = []
    for i in range(1, len(seq) - 1):
        if seq[i-1] < seq[i] > seq[i+1]:
            total_peaks += 1
            temp_buffer.append(seq[i])
    average_peak = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    return total_peaks, average_peak

def validate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    stable = variance < 50
    return stable, variance

def calculate_performance(data):
    # Extract key metrics
    raw_values = [d['value'] for d in data]
    weights = [d.get('weight', 1.0) for d in data]
    
    weighted_sum = sum(val * wt for val, wt in zip(raw_values, weights))
    base_average = sum(raw_values) / len(raw_values)
    
    # Misleading intermediate calculations (distraction)
    dummy_pairs = list(combinations(raw_values, 2))
    pair_sums = [a + b for a, b in dummy_pairs if a % 10 == 0]
    phantom_metric = len(pair_sums) * 0.75 if pair_sums else 0
    
    # Real processing branch
    peak_count, avg_peak = analyze_sequence(raw_values)
    is_stable, var_score = validate_stability(raw_values)
    
    # Simulate conditional logic with distractors
    adjustment_factor = 1.2 if base_average > 50 else 0.8
    stability_bonus = 10 if is_stable and peak_count >= 3 else 0
    
    # Dead code path (never executed, but looks relevant)
    debug_mode = False
    if debug_mode:
        print("Debug:", raw_values[:3])
        extra_correction = sum(1 for v in raw_values if v < 0)
    
    # Core computation chain
    preliminary_score = weighted_sum * adjustment_factor
    refined_score = preliminary_score + stability_bonus - var_score * 0.5
    final_score = int(refined_score - phantom_metric * 0.1)  # Minor influence to justify inclusion
    
    # Additional red herring: string-based filtering that doesn't affect outcome
    labels = ''.join([d.get('label', '') for d in data])
    valid_chars = len([c for c in labels if c.isupper()])
    char_penalty = valid_chars * 0.05
    
    return final_score

def main():
    benchmark_data = [
        {'value': 45, 'weight': 1.1, 'label': 'A1'},
        {'value': 67, 'weight': 0.9, 'label': 'B2'},
        {'value': 34, 'weight': 1.0, 'label': 'C3'},
        {'value': 89, 'weight': 1.2, 'label': 'D4'},
        {'value': 23, 'weight': 0.8, 'label': 'E5'},
        {'value': 76, 'weight': 1.0, 'label': 'F6'},
        {'value': 55, 'weight': 1.0, 'label': 'G7'}
    ]
    
    # Extraneous pre-processing
    sorted_data = sorted(benchmark_data, key=lambda x: x['value'], reverse=True)
    median_value = sorted_data[len(sorted_data)//2]['value']
    
    # Key execution point
    final_score = calculate_performance(benchmark_data)
    
    # Output result as required
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()