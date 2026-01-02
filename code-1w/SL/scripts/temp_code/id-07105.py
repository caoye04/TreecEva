import math

# Simulated data stream representing system performance metrics
data_stream = [
    (120, 85, 3), (98, 92, 2), (145, 77, 4), (110, 88, 3), (132, 80, 5)
]

# Auxiliary constants (some are distractions)
MAX_CAPACITY = 200
MIN_THRESHOLD = 50
WEIGHT_FACTOR = 0.85
DUMMY_OFFSET = 17  # Unused in final computation, red herring
TEMP_BUFFER = []   # Dead code path, never used

# Lambda functions for dynamic calculations
calculate_load_ratio = lambda x: x[0] / MAX_CAPACITY
calculate_stress_index = lambda x: (x[0] - x[1]) * x[2]
evaluate_efficiency = lambda lr, si: lr * (1 + si / 100)

# Helper function with nested logic
def analyze_records(records):
    cumulative = 0
    stress_values = []
    temp_sum = 0  # Intermediate tracker, partially irrelevant

    for record in records:
        load_ratio = calculate_load_ratio(record)
        stress_index = calculate_stress_index(record)
        
        # Track stress values for potential analysis (only max used later)
        stress_values.append(stress_index)
        
        # Irrelevant accumulation (not used in final result)
        temp_sum += record[1] * 0.1  
        
        # Core contribution to final score
        efficiency = evaluate_efficiency(load_ratio, stress_index)
        cumulative += efficiency
    
    # Distraction: unused average calculation
    avg_stress = sum(stress_values) / len(stress_values) if stress_values else 0
    peak_stress = max(stress_values) if stress_values else 0
    
    return cumulative, peak_stress

# Secondary function with misleading parameters
def adjust_for_environment(base_value, dummy_flag=False, scale=1.0):
    adjustment_curve = lambda x: math.log(x + 1) if x > 0 else 0
    adjusted = base_value * adjustment_curve(scale)
    return adjusted  # Not actually used; red herring

# Main processing pipeline
def process_metrics(stream):
    total_efficiency, max_stress = analyze_records(stream)
    
    # Distractor variables
    normalized_max = max_stress / 100
    dummy_correction = normalize_max ** 0.5  # Misspelled variable: harmless dead code
    
    # Actual efficiency score computation
    efficiency_score = total_efficiency * WEIGHT_FACTOR
    
    # Additional distraction: conditional that doesn't affect outcome
    if len(stream) > 10:
        efficiency_score *= 0.9  # Never executes
    
    # Final irrelevant transformation
    final_normalized = round(efficiency_score, 4)
    
    return final_normalized

# Execution point of interest
final_output = process_metrics(data_stream)

# Print target result
Result: {final_output}