from collections import Counter

def calculate_initial_metrics(data_points):
    # Irrelevant intermediate calculations
    temp_sum = sum(data_points) * 2
    irrelevant_avg = temp_sum / len(data_points) if data_points else 0
    
    # Actual relevant calculation
    point_counter = Counter(data_points)
    unique_count = len(point_counter)
    most_common_freq = point_counter.most_common(1)[0][1] if point_counter else 0
    
    # Misleading variable
    misleading_total = temp_sum + unique_count + most_common_freq
    
    return (unique_count, most_common_freq, misleading_total)

def apply_adjustments(base_values, adjustment_factors):
    base1, base2, _ = base_values
    factor1, factor2 = adjustment_factors
    
    # Dead code path
    if factor1 > 100:
        unused_calc = base1 * base2 * factor1
    
    # Relevant calculations with distractions
    adjusted1 = base1 * factor1
    adjusted2 = base2 * factor2
    
    # Irrelevant intermediate
    temp_product = adjusted1 * adjusted2
    
    return (adjusted1, adjusted2, temp_product)

def calculate_final_score(metrics, adjustments, multiplier):
    # Unpack with distraction
    unique_count, most_common_freq, _ = metrics
    adj1, adj2, _ = adjustments
    
    # Core calculation with multiple steps
    weighted_unique = unique_count * multiplier
    weighted_freq = most_common_freq * (multiplier // 2)
    
    # Irrelevant bitwise operation
    bit_distraction = (weighted_unique ^ weighted_freq) & 0xFF
    
    # Actual final calculation
    final_score = (weighted_unique + weighted_freq) - bit_distraction
    
    # Misleading alternative calculation
    alternative_score = (adj1 + adj2) * multiplier
    
    return final_score

# Main execution with distractions
data_points = [5, 3, 5, 7, 3, 2, 5, 8, 5, 2]
adjustment_factors = (3, 2)
multiplier = 4

# Calculate metrics with irrelevant intermediate
metrics = calculate_initial_metrics(data_points)
print(f"Intermediate metrics: {metrics}")

# Apply adjustments with distraction
adjustments = apply_adjustments(metrics, adjustment_factors)
print(f"Adjustments applied: {adjustments}")

# Final calculation
final_score = calculate_final_score(metrics, adjustments, multiplier)
print(f"Result: {final_score}")