from itertools import combinations

# Simulate a tournament scoring system with complex validation
def validate_sequence(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# Generate derived metrics from raw inputs
def compute_efficiency(a, b, c):
    if a == 0:
        return 0
    efficiency = (b * c) / a
    return round(efficiency, 3)

# Determine ranking based on adjusted points
def calculate_ranking(raw_points, deductions):
    base_total = sum(raw_points)
    adjustment_factor = 1.0
    
    # Apply conditional penalty scaling
    if len(deductions) > 2:
        adjustment_factor = 0.95
    elif len(deductions) == 1:
        adjustment_factor = 0.98

    adjusted_total = base_total * adjustment_factor
    
    # Irrelevant combination generation (distractor)
    combo_count = len(list(combinations(raw_points, 2)))
    temp_debug = [compute_efficiency(x, x+1, 2) for x in raw_points]
    
    # Secondary correction based on parity clusters
    even_cluster = [p for p in raw_points if p % 2 == 0]
    odd_cluster = [p for p in raw_points if p % 2 == 1]
    
    # Misleading cluster score (not used in final result)
    cluster_imbalance = abs(len(even_cluster) - len(odd_cluster))
    balance_penalty = cluster_imbalance * 0.1
    
    # Final computation unaffected by above cluster logic
    raw_deduction_sum = sum(deductions)
    net_points = adjusted_total - raw_deduction_sum
    
    # Additional red herring: validate sortedness of deductions (unused)
    is_valid = validate_sequence(sorted(deductions))
    
    # Key assignment
    final_score = int(round(net_points))
    return final_score

# Input data
points = [12, 15, 18, 23, 17]
penalties = [5, 3, 8]

# Execute main logic
final_score = calculate_ranking(points, penalties)
print(f"Target result: {final_score}")