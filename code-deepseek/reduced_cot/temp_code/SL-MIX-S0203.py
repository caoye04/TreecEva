def calculate_weighted_score(values, weights):
    # Distractor: complex weight calculation that's not used in final result
    adjusted_weights = [w * 2 - 1 for w in weights]
    weighted_sum = sum(v * w for v, w in zip(values, adjusted_weights))
    normalization_factor = sum(adjusted_weights) * 1.5
    return weighted_sum / normalization_factor if normalization_factor else 0

def find_optimal_threshold(data_points):
    # Misleading: this function creates intermediate results but doesn't affect final answer
    sorted_data = sorted(data_points)
    thresholds = [(sorted_data[i] + sorted_data[i+1]) / 2 for i in range(len(sorted_data)-1)]
    variance_calc = sum((x - sum(data_points)/len(data_points))**2 for x in data_points)
    return thresholds[len(thresholds)//2] if thresholds else 0

def process_metrics(input_data):
    base_values = [item['value'] for item in input_data if item['category'] == 'primary']
    secondary_values = [item['value'] for item in input_data if item['category'] == 'secondary']
    
    # Dead code path: this calculation is never used
    combined_analysis = sum(base_values) * len(secondary_values) - 25
    
    # Relevant computation chain
    if base_values and secondary_values:
        max_primary = max(base_values)
        min_secondary = min(secondary_values)
        ratio_calc = max_primary / min_secondary if min_secondary else 0
        
        # Distractor: unused bitwise operation
        bit_shift_result = (int(ratio_calc) << 2) & 0xFF
        
        # Key logic with conditional expressions
        adjustment_factor = 3 if ratio_calc > 15 else 2
        core_result = (ratio_calc * adjustment_factor) + len(base_values) - len(secondary_values)
        
        # Final processing with enumerate
        indexed_correction = sum(i * val for i, val in enumerate(base_values[:3])) / 10
        final_value = core_result + indexed_correction
        
        return round(final_value, 2)
    return 0

# Main execution with misleading intermediate variables
sample_data = [
    {'category': 'primary', 'value': 8},
    {'category': 'primary', 'value': 12},
    {'category': 'secondary', 'value': 3},
    {'category': 'primary', 'value': 15},
    {'category': 'secondary', 'value': 4}
]

# Irrelevant calculations that don't affect final result
weight_distraction = calculate_weighted_score([5, 7, 9], [0.2, 0.3, 0.5])
threshold_distraction = find_optimal_threshold([2, 4, 6, 8, 10])
composite_multiplier = weight_distraction * threshold_distraction + 7

# Actual relevant data processing
composite_data = sample_data
final_analysis = process_metrics(composite_data)

print(f"Result: {final_analysis}")