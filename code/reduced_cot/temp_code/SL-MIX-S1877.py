from collections import defaultdict
import math

def compute_adjusted_discrepancy(department_records):
    # Initialize departmental discrepancy tracking
    dept_adjustments = defaultdict(float)
    
    # Apply adjustments
    for record in department_records:
        dept_id, quarter, adjustment = record
        if quarter <= 2:  # Apply higher weight to first half adjustments
            adjustment *= 1.5
        dept_adjustments[dept_id] += adjustment
    
    # Convert to list and sort by discrepancy magnitude
    sorted_depts = sorted(dept_adjustments.items(), key=lambda x: abs(x[1]), reverse=True)
    
    # Identify outliers (top 25% by magnitude)
    outlier_count = max(1, len(sorted_depts) // 4)
    outliers = sorted_depts[:outlier_count]
    
    # Calculate normalization factor
    total_magnitude = sum(abs(value) for _, value in sorted_depts)
    outlier_magnitude = sum(abs(value) for _, value in outliers)
    
    # Compute weighted average excluding outliers
    remaining_depts = sorted_depts[outlier_count:]
    weighted_sum = sum(value * (1 + math.log(abs(value) + 1)) for _, value in remaining_depts if value != 0)
    weights = sum(1 + math.log(abs(value) + 1) for _, value in remaining_depts if value != 0)
    
    # Final score calculation
    base_score = weighted_sum / weights if weights > 0 else 0
    normalization_factor = (total_magnitude - outlier_magnitude) / total_magnitude if total_magnitude > 0 else 1
    
    return round(base_score * normalization_factor, 2)

# Financial records: (department_id, quarter, adjustment_amount)
financial_data = [
    ('FIN', 1, -12.5),
    ('HR', 2, 8.3),
    ('IT', 3, -20.1),
    ('OPS', 4, 15.7),
    ('FIN', 2, -5.2),
    ('HR', 1, 3.9),
    ('IT', 4, -18.4),
    ('OPS', 3, 11.6),
    ('MKT', 2, -9.8),
    ('MKT', 4, 7.2)
]

final_score = compute_adjusted_discrepancy(financial_data)
print(f"Target result: {final_score}")