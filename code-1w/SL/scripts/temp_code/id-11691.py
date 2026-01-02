def evaluate_performance(data, base):
    adjustments = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            adjusted = (val - base) * 1.5
        else:
            adjusted = (val + base) / 2.0
        adjustments.append(round(adjusted))
    
    # Irrelevant transformation (distractor)
    temp_result = [x ** 0.5 for x in adjustments if x > 0]
    temp_sum = sum(temp_result)
    normalized = [x / (temp_sum + 1e-8) for x in temp_result]
    
    # Real computation path
    magnitude = sum(abs(x) for x in adjustments)
    penalty = len([x for x in adjustments if x < 0]) * 2
    bonus = len([x for x in adjustments if x > 10]) * 3
    
    # Another red herring: complex slicing with no effect
    slice_offset = len(adjustments) // 3
    phantom_slice = adjustments[slice_offset: -slice_offset] if slice_offset > 0 else adjustments
    phantom_sum = sum(phantom_slice) / (len(phantom_slice) + 1)
    
    # Actual score calculation
    raw_score = magnitude + bonus - penalty
    scaling_factor = 0.95
    final_score = int(raw_score * scaling_factor)
    
    return final_score

# Main execution
metrics = [12, 8, 15, 4, 20, 6]
baseline = 10

# Dead code path (misleading function call that does nothing)
def legacy_calculate(x): return None
dummy = legacy_calculate(metrics)

intermediate_weight = sum(metrics) / len(metrics)  # Semi-relevant but unused later

final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")