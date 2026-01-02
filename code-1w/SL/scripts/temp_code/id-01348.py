from itertools import combinations

# Simulate employee productivity and risk metrics across departments
def analyze_department_metrics(base_values):
    adjusted = [val * 1.1 for val in base_values if val > 0]
    filtered = [x for x in adjusted if x < 100]
    return sorted(filtered, reverse=True)

# Auxiliary function to compute risk exposure
def calculate_risk_index(values):
    if len(values) < 3:
        return 0.5
    pairs = list(combinations(values, 2))
    total_diff = sum(abs(a - b) for a, b in pairs)
    avg_diff = total_diff / len(pairs) if pairs else 0
    return round(avg_diff / 10, 4)

# Core evaluation logic
def evaluate_performance(output, risk):
    threshold = 85
    base_score = sum(o // 2 for o in output if o > 10)
    penalty = int(risk * 100)
    bonus = 10 if len(output) >= 5 else 5
    
    # Distractor: irrelevant computation chain
    temp_data = [o * risk for o in output]
    temp_sum = sum(t for t in temp_data if t > 20)
    shadow_score = temp_sum * 0.05  # Not used in final result
    
    # Another red herring: complex but unused filter
    masked_values = [o for i, o in enumerate(output) if i % 2 == 0 and o in output]
    compression_factor = len(masked_values) / len(output) if output else 0
    
    # Actual score calculation
    raw_score = base_score - penalty + bonus
    final_score = max(raw_score, 0)  # Prevent negative scores
    
    # More distractions: unused state tracking
    history_log = []
    for val in output:
        status = "high" if val > threshold else "low"
        history_log.append(f"{status}-{val}")
    
    return int(final_score)

# Input data: daily output units per employee
productivity = [92, 45, 67, 88, 76, 54, 90]

# Preprocess through analysis pipeline
processed_output = analyze_department_metrics(productivity)

# Compute auxiliary risk metric
risk_factor = calculate_risk_index(processed_output)

# Key statement
final_score = evaluate_performance(processed_output, risk_factor)

print(f"Result: {final_score}")